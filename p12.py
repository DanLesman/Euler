def num_divisors(n):
	i = 1
	divisors_count = 0
	while i * i <= n:
		if n % i == 0:
			if i == n/i:
				divisors_count += 1
			else:
				divisors_count += 2
		i += 1
	return divisors_count

def first_with_n_divisors(n):
	i = 0
	num = 0
	while num_divisors(num) < 500:
		num += i
		i += 1
	return num

print(first_with_n_divisors(500))
