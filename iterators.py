#	lessons:
#		iterators

def ids():
	#_ids = ['apple', 'kiwi', 'peach']
	_ids = ['number_' + str(x) for x in range(10)]
	for _id in _ids:
		yield _id 

if __name__ == '__main__':
	pass
