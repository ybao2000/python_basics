queue = []
queue.append('get up')
queue.append('brush teeth')
queue.append('wash face')
queue.append('use toilet')
queue.append('eat breakfast')
queue.append('go to bus station')
queue.append('take bus')
queue.append('get to school')
queue.append('take classes')
queue.append('lunch break')
queue.append('take bus')
queue.append('get home')

print(queue, type(queue))
while len(queue) > 0:
	item = queue.pop(0)
	print(item)