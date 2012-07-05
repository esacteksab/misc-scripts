#!/usr/bin/python

import sys
import glob
from socket import socket

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003
delay = 60
sock = socket()
try:
    sock.connect((CARBON_SERVER, CARBON_PORT))
except:
    print "Couldn't connect to %(server)s on port %(port)d , is carbon-agent.py running?" % {'server': CARBON_SERVER, 'port': CARBON_PORT}
    sys.exit(1)

files = glob.glob('/opt/graphite/storage/import_data/*')

for file in files:
    lines = []
    try:
        f = open(file, "r")
        for line in f:
            drtylines = line.rstrip('\n')
            lines.append(drtylines)
            data = '\n'.join(lines) + '\n'
        f.close()
        print "sending message"
        print 80 * '-'
        print data
        sock.sendall(data)
    finally:
        f.close()
