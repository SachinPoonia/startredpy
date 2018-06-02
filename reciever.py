#!/usr/bin/python2

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('127.0.0.1',8666))

for i in range(10):
	print s.recvfrom(1000)[0]
	exit(0)
