def gen_primes(max_num):
    primes = [2]
    n = 3
    while len(primes) < max_num:
        if all(n % p > 0 for p in range(3, int(n**.5)+1)):
            primes.append(n)

        n+=2

    return max(primes)

print(gen_primes(10001))