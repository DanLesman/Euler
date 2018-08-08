def sum_of_square(n):
	sum_of_square = 0;
	for i in range (1,n+1):
		sum_of_square += i ** 2
	return sum_of_square

def square_of_sum(n):
	sum_to_n = (n * (n + 1)) / 2
	return sum_to_n ** 2

print (square_of_sum(100) - sum_of_square(100))