def gen_primes(N):
    for n in range(2, N):
        if all(n % p > 0 for p in range(2, n)):
            yield n


def smallest_multiple(max_number):
    primes_gen = gen_primes(max_number)
    numbers_list = set(range(2, max_number+1))
    multiples = 1
    prime = 1

    while len(numbers_list) > 1:
        if prime not in numbers_list:
            prime = next(primes_gen)

        numbers_list = {num // prime if num % prime == 0
                        else num for num in numbers_list}
        multiples *= prime

    return multiples


print(smallest_multiple(42))
