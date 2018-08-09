def get_prime_factors(n):
    factors = []

    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            factors.append(i)
        else:
            i += 1

    factors.append(n)
    return factors

def get_count_by_value(values):
    count_by_value = {}
    for value in values:
        count_by_value.setdefault(value, 0)
        count_by_value[value] += 1
    return count_by_value

def get_smallest_multiple(n):
    total_count_by_value = {}

    for x in xrange(2, n):
        factors = get_prime_factors(x)
        count_by_value = get_count_by_value(factors)
        for value, count in count_by_value.iteritems():
            total_count_by_value.setdefault(value, 0)
            total_count_by_value[value] = max(total_count_by_value[value], count)

    product = 1
    for value, count in total_count_by_value.iteritems():
        product *= value ** count

    return product

print [get_prime_factors(x) for x in xrange(1, 10)]
print [get_count_by_value(get_prime_factors(x)) for x in xrange(1, 10)]

print get_smallest_multiple(10)
print get_smallest_multiple(20)

