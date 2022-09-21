def jacob_symbol(a, b):
    if a <= 1:
        return a
    if (a % 2) != 0:
        amod4 = a % 4
        bmod4 = b % 4
        bmoda = b % a
        print(f"{a} is odd -- {a} mod 4 = {amod4} -- {b} mod 4 = {bmod4}")
        if amod4 == 3 and amod4 == bmod4:
            print(f"-jaco({bmoda}, {a})")
            return -jacob_symbol(bmoda, a)
        else:
            print(f"jaco({bmoda}, {a})")
            return jacob_symbol(bmoda, a)
    elif b % 8 == 1 or b % 8 == 7:
        print(f"{a} is even -- a/2 = {a/2} -- {b} mod 8 = +1/-1")
        print(f"jaco({a/2}, {b})")
        return jacob_symbol(a/2, b)
    else:
        print(f"{a} is even -- a/2 = {a / 2} -- {b} mod 8 != +1/-1")
        print(f"-jaco({a/2}, {b})")
        return -jacob_symbol(a/2, b)

def normalize_mod(a, N):
    return a % N, N

def all_value(id, N):
    a1, _ = normalize_mod(id, N)
    a2, _ = normalize_mod(-id, N)
    a3, _ = normalize_mod(id*3, N)
    a4, _ = normalize_mod(-id*3, N)
    return [a1, a2, a3, a4]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--ID', type=int, help='student ID')
    args = parser.parse_args()
    args.ID = 260890776

    checklist = all_value(args.ID, 262915409)
    print(checklist)
    symbols = []
    for y in checklist:
        symbol = jacob_symbol(y, 262915409)
        symbols.append(symbol)
    print(dict(zip(checklist, symbols)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
