def fib_seq_ntimes(n):
	prev = 0
	curr = 1
	for i in xrange(1,n):
		curr += prev
		prev = curr - prev
	return curr

def fib_seq_ton(n):
	prev = 0
	curr = 1
	while curr < n:
		curr += prev
		prev = curr - prev
	return curr

import time
start = time.time()
fib_seq_ntimes(1000)
print("{}".format(time.time()-start))