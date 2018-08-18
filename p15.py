def ways_to_get(n):
	ways = 1
	divideby = 1
	for i in range(1, n+1):
		ways *= i
	for x in range(1, (n/2)+1):
		divideby *= x
	return ways/(divideby**2)

print ways_to_get(40)
