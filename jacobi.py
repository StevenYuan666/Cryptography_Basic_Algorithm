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
        print(label[i], jacobi_symbol(e, 262915409))


if __name__ == '__main__':
    quadratic_residue(260921269)
    print("3s", jacobi_symbol(256932989, 16111), jacobi_symbol(256932989, 16319))
    print("-3s", jacobi_symbol(5982420, 16111), jacobi_symbol(5982420, 16319))
    print(jacobi_symbol(3, 262915409))
    print(jacobi_symbol(3, 16111))
    print(jacobi_symbol(3, 16319))
