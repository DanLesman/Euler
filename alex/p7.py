def get_n_primes(n):
    primes = [2, 3]

    i = 5
    to_add = 2
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)

        i+= to_add
        to_add = to_add % 4 + 2

    return primes



def is_prime(n, smaller_primes):
    for p in smaller_primes:
        if p * p > n:
            return True

        if n % p == 0:
            return False

    raise Exception('how did we get here?')

primes = [2, 3, 5, 7, 11, 13, 17, 19]
for x in xrange(2, 10):
    print x, is_prime(x, primes)


print get_n_primes(10001)[-1]

"""
n   2 3
1
2   x
3     y
4   x
5
6   x y
7
8   x
9     y
10  x
11
12  x y
13
14  x
15    y
16  x
17
"""
