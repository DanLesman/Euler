from operator import mul

def smallest_num_div_by_all(n):
	primelist = primes_in_range(n)
	smallest = reduce(mul, primes_in_range(n), 1)
	for i in range(1,n+1):
		for j in range (0,len(primelist)):
			if is_power_of(i, primelist[j]):
				smallest = smallest * primelist[j]
	return smallest

def primes_in_range(n):
	primes = [i for i in range(1,n+1) if is_prime(i)]
	return primes

def is_power_of(m, n):
	i = 2
	while n**i <= m and n != 1:
		if n**i == m:
			return True
		else:
			i += 1
	return False


def is_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		else:
			i += 1
	return True

print(smallest_num_div_by_all(20))
