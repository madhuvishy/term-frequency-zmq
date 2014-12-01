import zmq

class Splitter(object):

    def __init__(self):
        self.context = zmq.Context()
        self.sender = self.context.socket(zmq.PUSH)
        self.sink = self.context.socket(zmq.PUSH)
        self.sender_address = "tcp://*:5557"
        self.sink_address = "tcp://localhost:5558"

    def bind_and_connect(self):
        self.sender.bind(self.sender_address)
        self.sink.connect(self.sink_address)

    def read_file(self, file_path):
        with open(file_path) as f:
            return f.read()

    def split(self, line):
        pass

    def partition(self, file_data):
        print("Press enter when workers are ready...")
        raw_input()
        self.sink.send_string(u'Connecting source and sink')
        lines = file_data.split("\n")
        for i in range(len(lines)):
            print lines[i]
            self.sender.send_string(u'%s' % lines[i])

splitter = Splitter()
splitter.bind_and_connect()
splitter.partition(splitter.read_file("input.txt"))
