import zmq

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

    def map_task(self):
        while True:
            s = self.source.recv()
            self.sink.send(s)
    
map_worker = MapWorker()
map_worker.connect()
map_worker.map_task()
