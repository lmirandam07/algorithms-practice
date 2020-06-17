from math import prod

def prime_factors(max_num, divider = 2):
    total = 1
    if max_num == 1: return 1

    while max_num > 1:
        exponents = 0
        while max_num % divider == 0:
            exponents += 1
            max_num /= divider

        divider += 1
        total*= (exponents + 1)
    return total

def highly_triangular(max_divisor):
    divisors = 0
    cont = 0
    while(divisors <= max_divisor):
        cont += 1
        if cont % 2 != 0:
            divisors = prime_factors(cont) * prime_factors((cont+1)/2)
        else:
            divisors = prime_factors(cont/2) * prime_factors(cont+1)


    return (cont*(cont+1))/2



print(highly_triangular(500))
