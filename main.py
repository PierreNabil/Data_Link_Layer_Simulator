from datalink import DataLinkLayer
from protocol import FrameKind

MAX_TIME = 100

# [(t1, packet1), (t2, packet2), ...]
network_layer_for_computer = [
	[(0, c) for c in 'Hello World!'] + [(30, c) for c in 'HAHA!'],
	[(0, c) for c in 'Welcome.']
]

# {t_i, t_j, t_k, ...}
error_times_for_computer = [
	{2, 32},
	{3,  9}
]

computer = [
	DataLinkLayer(0, network_layer_for_computer[0]),
	DataLinkLayer(1, network_layer_for_computer[1])
]

wire_from = [
	None,
	None
]


for t in range(MAX_TIME):
	i = t % 2

	events = computer[i].check_events(wire_from[1-i], t)
	wire_from[i] = computer[i].make_decision(events, wire_from[1-i], t)

	if (wire_from[i] is not None) and (t in error_times_for_computer[i]):
		wire_from[i].kind = FrameKind.err

print(computer[0].network_layer_data_received)
print(computer[1].network_layer_data_received)
