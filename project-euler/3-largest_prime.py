def largest_prime_factor(MAX, divider = 2):
    prime_factors = []

    while MAX > 1:
        while MAX % divider == 0:
            prime_factors.append(divider)
            MAX /= divider
        divider += 1

    return prime_factors

print(largest_prime_factor(600851475143))