import zmq
import pickle

class MapWorker(object):

    def __init__(self):
        self.context = zmq.Context()
        self.source = self.context.socket(zmq.PULL)
        self.sink = self.context.socket(zmq.PUSH)
        self.source_address = "tcp://localhost:5557"
        self.sink_address = "tcp://localhost:5558"

    def connect(self):
        self.source.connect(self.source_address)
        self.sink.connect(self.sink_address)

    def mapped(self, line):
        words = line.split(" ")
        return filter((lambda w : w[0] != ""),
                      map((lambda w : [w, 1]), words))

    def worker(self):
        while True:
            s = self.source.recv()
            self.sink.send(pickle.dumps(self.mapped(s)))

map_worker = MapWorker()
map_worker.connect()
map_worker.worker()
