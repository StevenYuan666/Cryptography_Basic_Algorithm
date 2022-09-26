def modExp(modulus: int, base: int, exponent: int):
    x = base
    t = 1
    while exponent > 0:
        if exponent % 2 == 1:
            t = t * x % modulus
            exponent = exponent - 1
        x = x ** 2 % modulus
        exponent = exponent // 2

    return t


if __name__ == '__main__':
    p = 16111
    q = 16319
    # print(modExp(modulus=p, base=5239, exponent=4028))
    # print(modExp(modulus=q, base=9666, exponent=4080))

    print((54153561 ** 2 % 262915409) == ((-3 * 260921269) % 262915409))
    print((48392954 ** 2 % 262915409) == ((-3 * 260921269) % 262915409))
    print((208761848 ** 2 % 262915409) == ((-3 * 260921269) % 262915409))
    print((214522455 ** 2 % 262915409) == ((-3 * 260921269) % 262915409))
