from protocol import *


class DataLinkLayer:
	def __init__(self, comp_id, network_layer_data, timer_max_wait=3):
		self.ID = comp_id

		self.next_frame_to_send = 0
		self.ack_expected = 0
		self.frame_expected = 0
		self.buffer = [None]*(MAX_SEQ+1)
		self.n_buffered = 0

		self.time_stamps = [] #[(t1, seq1), (t2, seq2), ...]
		self.timer_frame_no = None
		self.timer_max_wait = 2 * timer_max_wait - 1
		self.timer_i = None

		self.network_layer_data_to_send = network_layer_data #[(t1,packet1), (t2,packet2), ...]
		self.network_layer_data_received = []
		self._enable_network_layer()

	def _start_timer(self, seq, t):
		self.time_stamps.append((t, seq))

	def _stop_timer(self, seq, t):
		indexes_to_pop = []
		for i, (ti, seqi) in enumerate(self.time_stamps):
			if seqi == seq:
				indexes_to_pop.append(i)
			elif ti < t:
				indexes_to_pop.append(i)
		for i in reversed(indexes_to_pop):
			self.time_stamps.pop(i)

	def _is_timeout(self, t):
		if self.time_stamps:
			if self.timer_i is not None:
				return True
			elif t > self.time_stamps[0][0] + self.timer_max_wait:
				return True
		return False

	def check_events(self, input_frame, t):
		events = []
		if input_frame is not None:
			# print('@t=', t, '\t: C' + str(self.ID) + ' Received:', input_frame)
			if input_frame.kind is not FrameKind.err:
				events.append(EventType.frame_arrival)
			else:
				events.append(EventType.checksum_error)
		if self._is_timeout(t):
			events.append(EventType.timeout)
		elif self._is_network_layer_ready(t):
			events.append(EventType.network_layer_ready)
		return events

	def _send_data(self, frame_no, frame_expected, buffer, t):
		kind = FrameKind.data
		ack = (frame_expected + MAX_SEQ) % (MAX_SEQ + 1)
		s = Frame(kind, frame_no, ack, buffer[frame_no])
		self._start_timer(frame_no, t)
		return s

	def _enable_network_layer(self):
		self.network_layer_is_enabled = True

	def _disable_network_layer(self):
		self.network_layer_is_enabled = False

	def _is_network_layer_ready(self, t):
		if self.network_layer_is_enabled and self.network_layer_data_to_send:
			if t >= self.network_layer_data_to_send[0][0]:
				return True
		return False

	def _from_network_layer(self, t):
		if not self._is_network_layer_ready(t):
			raise ReferenceError('Called Network Layer While Not ready.')
		packet = self.network_layer_data_to_send[0][1]
		self.network_layer_data_to_send.pop(0)
		return packet

	def _to_network_layer(self, packet, t):
		self.network_layer_data_received.append((t, packet))

	def make_decision(self, events, input_frame, t):
		s = None

		if EventType.timeout in events:
			if self.timer_i is None:
				self.next_frame_to_send = self.ack_expected
				self.timer_i = 1
			s = self._send_data(self.next_frame_to_send, self.frame_expected, self.buffer, t)
			self.next_frame_to_send = inc(self.next_frame_to_send)
			self.timer_i += 1
			if self.timer_i > self.n_buffered:
				self.timer_i = None

		elif EventType.network_layer_ready in events:
			self.buffer[self.next_frame_to_send] = self._from_network_layer(t)
			self.n_buffered += 1
			s = self._send_data(self.next_frame_to_send, self.frame_expected, self.buffer, t)
			self.next_frame_to_send = inc(self.next_frame_to_send)

		if EventType.frame_arrival in events:
			r = input_frame
			if r.seq == self.frame_expected:
				self._to_network_layer(r.info, t)
				if s:
					s.ack = self.frame_expected
				else:
					s = Frame(FrameKind.ack, None, r.seq, None)
				self.frame_expected = inc(self.frame_expected)
			while between(self.ack_expected, r.ack, self.next_frame_to_send):
				self.n_buffered -= 1
				self._stop_timer(self.ack_expected, t)
				self.ack_expected = inc(self.ack_expected)

		elif EventType.checksum_error in events:
			pass

		if self.n_buffered < MAX_SEQ:
			self._enable_network_layer()
		else:
			self._disable_network_layer()

		# if s is not None or self.next_frame_to_send != []:
		# 	print('@t={:02d}: C{} Sent: {}'.format(t, self.ID, s))
		return s

	def get_data_received(self):
		s = ''
		for ti, pi in self.network_layer_data_received:
			s += str(pi)
		return s