#!/bin/python2

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#for i in range(100):
#	msg=raw_input('enter your msg: ')
#	s.sendto(msg,('127.0.0.1',6666)
#	print s.recvfrom(1000)

n1=raw_input('Enter your message here: ')

s.sendto(n1,('127.0.0.1',8666))


