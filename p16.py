def sum_numbers_in_power(n):
	toadd = str(2**n)
	total = 0
	for i in range(len(toadd)):
		total += int(toadd[i])
	return total

print sum_numbers_in_power(1000)
