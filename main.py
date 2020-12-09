from datalink import DataLinkLayer
from protocol import FrameKind

MAX_TIME = 100

# [(t1, packet1), (t2, packet2), ...]
network_layer_for_computer1 = [(0, c) for c in 'Hello World!'] #+ [(30, c) for c in 'HAHA']
network_layer_for_computer2 = [(0, c) for c in 'Welcome.']

# {t_i, t_j, t_k, ...}
error_times_for_computer_1 = {2, 32}
error_times_for_computer_2 = {3, 9}


computer1 = DataLinkLayer(1, network_layer_for_computer1)
computer2 = DataLinkLayer(2, network_layer_for_computer2)

wire_from_1_to_2 = None
wire_from_2_to_1 = None

for t in range(MAX_TIME):
	events = computer1.check_events(wire_from_2_to_1, t)
	wire_from_1_to_2 = computer1.make_decision(events, wire_from_2_to_1, t)

	if t is not None and t in error_times_for_computer_1:
		wire_from_1_to_2.kind = FrameKind.err

	events = computer2.check_events(wire_from_1_to_2, t)
	wire_from_2_to_1 = computer2.make_decision(events, wire_from_1_to_2, t)

	if t is not None and t in error_times_for_computer_2:
		wire_from_2_to_1.kind = FrameKind.err

print(computer1.network_layer_data_received)
print(computer2.network_layer_data_received)
