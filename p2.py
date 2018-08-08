previous = 0
current = 1
total = 0
while current < 4000000:
	if current % 2 == 0:
		total+=current
	nxt = previous + current
	previous = current
	current = nxt	

def fib_seq_ntimes(n):
	prev = 0
	curr = 1
	for i in xrange(1,n)
		curr += prev
		prev = curr - prev
	return curr

def fib_seq_ton(n):
	prev = 0
	curr = 1
	while curr < n
		curr += prev
		prev = curr - prev
	return curr

print(total)