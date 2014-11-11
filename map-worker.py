import zmq

context = zmq.Context()

source = context.socket(zmq.PULL)
source.connect("tcp://localhost:5557")

sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

while True:
    s = source.recv()
    sink.send(s)
