"""
Test server for the client thread sample

Eli Bendersky (eliben@gmail.com)
This code is in the public domain
"""
from socket import *
import time
import sys

from hl7.ack import ACK
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(2)

while True:
    connection, address = sockobj.accept()
    print 'Server connected by', address

    while connection:
        try:
            d = connection.recv(1024)
            if not d:
                break
            print d
        except:
            sys.exc_info()

        time.sleep(.5)
        if len(d):
            ack = ACK(d)
            connection.send(ack)
#connection.send('\x04\x00\x00\x00tuxy')
