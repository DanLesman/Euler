import math

def get_largest_factor(n):
	largest_factor = 0
	for i in range(2,int(math.sqrt(n))+1):
		if n % i == 0:
			if is_prime(n/i) and n/i > largest_factor:
				largest_factor = n/i
			if is_prime(i) and i > largest_factor:
				largest_factor = i
	return largest_factor

def is_prime(n):
	for i in range(2,int(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

print(get_largest_factor(600851475143))