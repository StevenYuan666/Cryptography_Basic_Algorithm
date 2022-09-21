def jacobi_symbol(a: int, b: int):
    if a <= 1:
        return a
    if a % 2 == 1:
        if (a % 4) == (b % 4) == 3:
            return -1 * jacobi_symbol(b % a, a)
        else:
            return jacobi_symbol(b % a, a)
    elif (b % 8 == 1) or (b % 8 == 7):
        return jacobi_symbol(a // 2, b)
    else:
        return -1 * jacobi_symbol(a // 2, b)


def calculate_s(s):
    result = [s % 262915409, (-s + 262915409) % 262915409, ((3 * s) % 262915409)]
    last = -3 * s
    while last < 0:
        last += 262915409
    result.append(last % 262915409)
    return result


def quadratic_residue(s):
    all_s = calculate_s(s)
    label = ["s", "-s", "3s", "-3s"]
    for i, e in enumerate(all_s):
        print(label[i], jacobi_from_web(e, 262915409))


def jacobi_from_web(a, n):
    assert (n > a > 0 and n % 2 == 1)
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0


if __name__ == '__main__':
    # print(calculate_s(260921269))
    quadratic_residue(260907962)
    # print("3s", jacobi_symbol(256932989, 16111), jacobi_symbol(256932989, 16319))
    # print("-3s", jacobi_symbol(5982420, 16111), jacobi_symbol(5982420, 16319))
