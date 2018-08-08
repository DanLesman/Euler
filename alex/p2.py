def get_nth_fib(n):
    prev = 1
    curr = 1
    for i in xrange(n):
        curr = curr + prev
        prev = curr - prev

    return curr

def compute_sum_of_evens_less_than_value(val):
    n = 1
    total = 0
    while True:
        nth_fib = get_nth_fib(n)
        if nth_fib > val:
            break

        total += nth_fib
        n += 3

    return total

def compute_sum_of_evens_of_first_n_terms(n):
    return sum((get_nth_fib(x) for x in xrange(1, n, 3)))


import time
for exp in xrange(1):
    start = time.time()
    n = 1000 * 2 ** exp
    compute_sum_of_evens_of_first_n_terms(n)
    print("N: {} - {}".format(n, time.time()-start))
