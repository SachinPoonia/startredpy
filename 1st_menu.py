#!/usr/bin/python2

import time,os

print'''
Press 1: Show the current time
Press 2: Reboot the OS
Press 3: To create user in OS
'''

input1 = int(raw_input('Your choice : '))

if input1 == 1:
	x = time.ctime()
	x1 = x.split()[3]
	print x1

elif input1 == 2:
	print 'The system will reboot now...'
	time.spleep(2)
	os.system('reboot')
	
elif input1 == 3:
	x = ['tom','jerry']
	for i in x:
		os.system('useradd ' +i)
		print i + ' user is added.'

else:
	print 'Wrong Choice'
