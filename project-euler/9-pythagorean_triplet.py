'''
Usando la fórmula Euclideana para encontrar tripletes Pitagóricos sabemos que
Dado dos números m y n donde m > n
a = m^2 - n^2
b = 2mn
c = m^2 + n^2
Entonces si a + b + c = n tenemos que
m^2 - n^2 + 2mn + m^2 + n^2 = n
m^2 + 2mn + m^2 = n
2m(m + n) = n
m(m + n) = n/2
'''

def pyth_triplet(number):
    for m in range(2, number):
        for n in range(2, m):
            if m*(m+n) == number/2:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
                return a, b, c

print(pyth_triplet(2000))