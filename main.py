from math import sqrt
from math import gcd


def primitive_roots(modulo):
    required_set = {num for num in range(1, modulo) if gcd(num, modulo)}
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]


def gen_primes(a=99999):
    prime_array = []
    for i in range(2, a):
        for x in range(2, int(sqrt(i)) + 1):
            if i % x == 0:
                break
        else:
            prime_array.append(i)
    return prime_array


if __name__ == '__main__':
    primes = gen_primes()

    while True:
        n_num = input("Choose prime number (up to 99999): \n")
        n_num = int(n_num)
        if n_num in primes:
            break
        else:
            print("Given number is not prime.")

    p_roots = primitive_roots(n_num)
    print("Primitive roots modulo " + str(n_num) + ": \n", p_roots)

    while True:
        p_num = input("Choose primitive root: \n")
        p_num = int(p_num)
        if p_num in p_roots:
            break
        else:
            print("Given number is not primitive root modulo ", n_num)

    while True:
        PkXa = int(input("Enter Private key A: "))
        if PkXa >= n_num:
            print("Given number is too large. Must be less than ", n_num)
        else:
            break

    while True:
        PkXb = int(input("Enter Private key B: "))
        if PkXb >= n_num:
            print("Given number is too large. Must be less than ", n_num)
        else:
            break

    ya = p_num ** PkXa % n_num
    yb = p_num ** PkXb % n_num

    ka = yb ** PkXa % n_num
    kb = ya ** PkXb % n_num

    print("Public Key A: ", ya)
    print("Public Key B: ", yb)
    print("Shared secret key A: ", ka)
    print("Shared secret key B: ", kb)
    