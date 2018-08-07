def is_palindrome(n):
    return str(n) == str(n)[::-1]

maximum = 0
for i in xrange(999, 99, -1):
    for j in xrange(999, 99, -1):
        if is_palindrome(i*j):
            maximum = max(i*j, maximum)

print maximum
