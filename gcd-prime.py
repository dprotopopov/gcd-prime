# Finding prime numbers using GCD algorithm
# Copyrigth(c) 2019, Dmitry Protopopov <dmitry@protopopov.ru>

import math

prod = 1

with open('primes.txt', 'w') as f:
    for i in range(2, 1000000):
        if (math.gcd(i, prod) == 1):
            prod *= i
            f.write(str(i) + '\n')
    f.close()
