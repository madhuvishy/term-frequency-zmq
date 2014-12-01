import zmq

class Reducer(object):

    def __init__(self):
        self.context = zmq.Context()
        self.sink = self.context.socket(zmq.PULL)
        self.sink_address = "tcp://*:5558"

    def bind(self):
        self.sink.bind(self.sink_address)

    def reduce_task(self):
        accumalator = []
        print self.sink.recv()
        for i in range(int(self.sink.recv())):
            s = self.sink.recv()
            accumalator.append(s)
        print accumalator

reducer = Reducer()
reducer.bind()
reducer.reduce_task()
