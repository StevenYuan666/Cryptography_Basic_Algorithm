def find_inverse(p: int, a: int):
    if a > p:
        a = a % p
    for i in range(1, p):
        if i * a % p == 1:
            return i


if __name__ == '__main__':
    print("p^(-1) mod q =", find_inverse(p=16319, a=16111))
    print("q^(-1) mod p =", find_inverse(p=16111, a=16319))
