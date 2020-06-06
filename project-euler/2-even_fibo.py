def even_fibo():
    MAX = 4*(10**6)
    a = 1
    b = 2
    acc = 0
    while(a < MAX):
        temp = b
        b += a
        a = temp
        if a % 2 == 0:
            acc += a

    return acc

print(even_fibo())