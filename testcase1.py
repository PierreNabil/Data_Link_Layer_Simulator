# defines test case for the program

# [(t1, packet1), (t2, packet2), ...] for each computer
network_layer_for_computer = [
	[(0, c) for c in 'Hello World!'] + [(35, c) for c in ' HAHA'],
	[(0, c) for c in 'Welcome '] + [(40, c) for c in 'to the jungle.']
]

# {t_i, t_j, t_k, ...}
# even numbers affect C0, while odd numbers affect C1
error_times = {2, 5, 38, 67}