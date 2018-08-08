import math
for c in range(1,1000):
	for a in range(1, c):
		for b in range(1+a, c):
			if a*a + b*b == c*c and a+b+c == 1000:
				print(a*b*c)
