import zmq
import sys

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
        print("Press enter when workers are ready...")
        raw_input()
        self.sink.send_string(u'Connecting source and sink')

    def read_file(self, file_path):
        with open(file_path) as f:
            return f.read()

    def split(self, file_data):
        lines = filter((lambda l:l != ""), file_data.split("\n"))
        self.sink.send_string(u'%i' % len(lines))
        for i in range(len(lines)):
            self.sender.send_string(u'%s' % lines[i])

reload(sys)
sys.setdefaultencoding('UTF8')

splitter = Splitter()
splitter.bind_and_connect()
splitter.split(splitter.read_file(sys.argv[1]))
