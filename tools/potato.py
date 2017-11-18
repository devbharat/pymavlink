from sseclient import SSEClient
import simplejson as json
from ast import literal_eval

import socket
import sys
import os

import cPickle
import time

#server_address = '/home/carl/src/devbharat_pymavlink/mavlink/potato_socket'
server_address = '127.0.0.1'
server_port = 14340
# Create a UDS socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setblocking(0)
# Connect the socket to the port where the server is listening
print('connecting to server_address')
while True:
    try:
        sock.connect((server_address, server_port))
        break
    except socket.error, msg:
        print('sys.stderr, msg')

while True:
    a = "adasdghakshdbjvaskfhb"
    picklebuf = cPickle.dumps(a)
    k= cPickle.loads(picklebuf)
    sock.sendall(picklebuf)
    time.sleep(4)
    print('send')

messages = SSEClient('https://api.particle.io/v1/devices/events?access_token=aa7aded201ea079970fd9ed760037f4cc9d97477')
for msg in messages:
    outputMsg = msg.data
    if type(outputMsg) is not str:
        outputJS = json.loads(outputMsg)
        FilterName = "data"
        #print( FilterName, outputJS[FilterName] )
        #print(outputJS[FilterName])
        a = literal_eval(outputJS[FilterName])
        picklebuf = cPickle.dumps(a)
        k= cPickle.loads(picklebuf)
        print(k)
        sock.sendall(picklebuf)
        print "lat = "+str(a["lat"])
        print "lon = "+str(a["lon"])
        print "amsl = "+str(a["amsl"])
        print "head = "+str(a["head"])
        print "volts = "+str(a["volts"])

