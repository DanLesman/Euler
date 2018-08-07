def get_nth_fib(n):
    prev = 1
    curr = 1
    for i in xrange(n):
        curr = curr + prev
        prev = curr - prev

    return curr

n = 1
total = 0
while True:
    nth_fib = get_nth_fib(n)
    if nth_fib > 4 * 10**6:
        break

    total += nth_fib
    n += 3


print get_nth_fib(1)
print get_nth_fib(4)
print total






