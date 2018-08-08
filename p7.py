def nth_prime(n):
	list_of_prime = []
	i = 1
	while len(list_of_prime) <= n:
		if is_prime(i):
			list_of_prime.append(i)
		i += 1
	return list_of_prime[n]


def is_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		else:
			i += 1
	return True

print(nth_prime(10001))