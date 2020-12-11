from enum import *

MAX_PKT = 1024
MAX_SEQ = 7


@unique
class FrameKind(Enum):
	data = auto()
	ack  = auto()
	nak  = auto()
	err  = auto()

	def __str__(self):
		return 'FrameKind.' + self.name


@unique
class EventType(Enum):
	frame_arrival = auto()
	checksum_error = auto()
	timeout = auto()
	network_layer_ready = auto()

	def __str__(self):
		return 'EventType.' + self.name

	def __repr__(self):
		return 'EventType.' + self.name


class Frame:
	def __init__(self, kind, seq, ack, info):
		self.kind = kind	#FrameKind()
		self.seq  = seq		#int
		self.ack  = ack		#int
		self.info = info	#list of data

	def __str__(self):
		if isinstance(self.info, str):
			info = "'" + self.info + "'"
		else:
			info = str(self.info)
		s = 'Frame(' + str(self.kind) + ',' + str(self.seq) + ',' + str(self.ack) + ',"' + info + '")'
		return s


def between(a, b, c):
	if (a <= b < c) or (c < a <= b) or (b < c < a):
		return True
	else:
		return False


def inc(k):
	if k < MAX_SEQ:
		return k + 1
	else:
		return 0
