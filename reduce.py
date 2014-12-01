import zmq
import pickle

class Reducer(object):

    def __init__(self):
        self.context = zmq.Context()
        self.sink = self.context.socket(zmq.PULL)
        self.sink_address = "tcp://*:5558"

    def bind(self):
        self.sink.bind(self.sink_address)

    def reduce_task(self):
        counts = {}
        for i in range(int(self.sink.recv())):
            print counts
            word_pairs = pickle.loads(self.sink.recv())
            for word, value in word_pairs:
                if counts.get(word) == None:
                    counts[word] = 1
                else:
                    counts[word] += 1
        print counts

reducer = Reducer()
reducer.bind()
reducer.reduce_task()
