def list_primes(n):
	#primes = [i for i in range(2,n) if is_prime(i)]
	primestemp = [2]
	primes = []
	for i in range(3,n,2):
			primestemp.append(i)
	for j in range(0,len(primestemp)):
		if is_prime(primestemp[j]):
			primes.append(primestemp[j])
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
