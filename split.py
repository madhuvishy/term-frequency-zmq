import zmq

context = zmq.Context()

sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Press enter when workers are ready...")
raw_input()

sink.send_string(u'Connecting source and sink')

for i in range(10):
    sender.send_string(u'%i' % i)
