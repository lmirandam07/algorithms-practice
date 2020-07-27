import math

def lattice_paths(n):
    n_fact = math.factorial(n)
    return math.factorial(2 * n) // (n_fact * n_fact)

print(lattice_paths(20))