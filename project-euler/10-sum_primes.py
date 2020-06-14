def gen_primes(max_num):
    primes = 2
    n = 3
    while n < max_num:
        if all(n % p > 0 for p in range(3, int(n**.5)+1)):
            primes+= n

        n+=2

    return primes

print(gen_primes(2000000))