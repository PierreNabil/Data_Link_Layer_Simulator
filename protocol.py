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
		return self.name


@unique
class EventType(Enum):
	frame_arrival = auto()
	checksum_error = auto()
	timeout = auto()
	network_layer_ready = auto()


class Frame:
	def __init__(self, kind, seq, ack, info):
		self.kind = kind	#FrameKind()
		self.seq  = seq		#int
		self.ack  = ack		#int
		self.info = info	#list of data

	def __str__(self):
		return 'Frame(kind=' + str(self.kind) + ',seq=' + str(self.seq) + ',ack=' + str(self.ack) + ',info=' + str(self.info) + ')'


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
