def largest_prime_factor(max_num, divider = 2):
    prime_factors = []

    while max_num > 1:
        while max_num % divider == 0:
            prime_factors.append(divider)
            max_num /= divider
        divider += 1

    return prime_factors

print(largest_prime_factor(600851475143))