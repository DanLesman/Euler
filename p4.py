def is_palindrome(n):
	for k in range (1,len(str(n))/2+1):
		if str(n)[k-1] is not str(n)[len(str(n))-k]:
			return False
	return True

largest_palindrome = 0
for i in range (100,1000):
	for j in range (100,1000):
		if is_palindrome(i*j) and i*j > largest_palindrome:
			largest_palindrome = i*j

print (largest_palindrome)