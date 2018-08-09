def list_primes(n):
	primes = [i for i in range(2,n) if is_prime(i)]
	return primes

def is_prime(n):
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		else:
			i += 1
	return True

print(sum(list_primes(2 * 10**6)))
