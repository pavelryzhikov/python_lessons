#	lessons:
#		iterators
#		fork()

import os
from iterators import *

def parent():
	x=ids()
	for i in x:
		newpid = os.fork()
		if newpid == 0:
			try:
				child(i)
			except:
				pass
		else:
			pids = (os.getpid(), newpid)
			print('parent: %d, child: %d\n' % pids)

def child(x):
	print('child',  x)
	os._exit(0)

if __name__ == '__main__':
	pass
