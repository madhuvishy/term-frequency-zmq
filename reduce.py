import zmq

context = zmq.Context()

sink = context.socket(zmq.PULL)
sink.bind("tcp://*:5558")

accumalator = []

print sink.recv()

for i in range(10):
    s = int(sink.recv())
    accumalator.append(s)

print reduce(lambda x, y: x+y, accumalator)
