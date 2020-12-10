from datalink import DataLinkLayer
from protocol import *

from testcase import *

MAX_TIME = 100

class SimulationReader:
    def __init__(self, datafilename='./data/data.txt'):
        self.file = open(datafilename, 'r')
        self.next_t = 0

    def get_specific_timestep(self, t):
        if self.next_t > t:
            self.reset()
            for _ in range(t):
                self.get_next_timestep()
            return self.get_next_timestep()
        else:
            for _ in range(t - self.next_t):
                self.get_next_timestep()
            return self.get_next_timestep()

    def get_next_timestep(self):
        t = eval(self.file.readline())
        computeri = t % 2
        self.next_t = t + 1

        network_layer_data_to_send = eval(self.file.readline())
        network_layer_data_received = eval(self.file.readline())

        events = eval(self.file.readline())
        buffer = eval(self.file.readline())
        n_buffered = eval(self.file.readline())
        next_frame_to_send = eval(self.file.readline())

        error = eval(self.file.readline())
        wire_fromi = eval(self.file.readline())

        self.file.readline()

        state = t, computeri, network_layer_data_to_send, network_layer_data_received, events, buffer, n_buffered, next_frame_to_send, error, wire_fromi
        return state

    def reset(self):
        self.file.seek(0)
        self.next_t = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_t < MAX_TIME:
            return self.get_next_timestep()
        else:
            raise StopIteration



def run_simulation():

    computer = [
        DataLinkLayer(0, network_layer_for_computer[0].copy()),
        DataLinkLayer(1, network_layer_for_computer[1].copy())
    ]

    wire_from = [
        None,
        None
    ]

    with open('./data/data.txt', 'w') as f:
        for t in range(MAX_TIME):
            i = t % 2

            events = computer[i].check_events(wire_from[1-i], t)
            wire_from[i] = computer[i].make_decision(events, wire_from[1-i], t)

            if (wire_from[i] is not None) and (t in error_times):
                wire_from[i].kind = FrameKind.err

            s = ('{}\n'*9 + '\n').format(
                t,

                computer[i].network_layer_data_to_send,
                "'" + str(computer[i].get_data_received()) + "'",

                events,
                computer[i].buffer,
                computer[i].n_buffered,
                computer[i].next_frame_to_send,

                t in error_times,
                wire_from[i]
            )
            f.write(s)


if __name__ == '__main__':
    run_simulation()
    reader = SimulationReader()

    for timestep in reader:
        print(timestep)

    print()

    print(reader.get_specific_timestep(5))
    print(reader.get_specific_timestep(7))

