def get_largest_factor(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
        else:
            i += 1

    return n

print(get_largest_factor(32))
print(get_largest_factor(600851475143))
