def sqr_root(p, a):
    if p % 4 == 3:
        return a ** ((p + 1) / 4) % p
    if p % 4 == 1:
        b = 260921269 * 3 % p  # since s is a quadratic non residue as shown before
        r = 8055
        r_prime = 0
        l = 0
        m = 8055
        for i in range(l, 0, -1):
            r = r // 2
            r_prime = r_prime // 2
            if (a ** r) * (b ** r_prime) % p == (p - 1):
                r_prime = r_prime + (2 ** l) * m

        return (a ** ((r + 1) // 2)) * (b ** (r_prime // 2)) % p


if __name__ == '__main__':
    # a = sqr_root(16111, ((-3 * 260921269) % 16111))
    # print(a)
    print((-3 * 260921269) % 16319)
