prev = 0
curr = 1
total = 0
while curr < 4000000:
	if curr % 2 == 0:
		total+=curr
	nxt = prev + curr
	prev = curr
	curr = nxt	
print(total)