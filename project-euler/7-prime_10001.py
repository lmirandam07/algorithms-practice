def gen_primes(max_num):
    primes = []
    n = 2
    while len(primes) < max_num:
        if all(n % p > 0 for p in range(2, int(n**.5)+1)):
            primes.append(n)

        n+=1

    return max(primes)

print(gen_primes(10001))