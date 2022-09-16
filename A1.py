def jacob_symbol(a, b):
    if a == 1 or a == 0:
        return a
    if (a % 2) != 0:
        amod4 = a % 4
        bmod4 = b % 4
        bmoda = b % a
        print(f"odd ----- {a} mod 4 = {amod4} ----- {b} mod 4 = {bmod4}")
        if amod4 == 3 and amod4 == bmod4:
            print(f"-jaco({bmoda}, {a}) \n")
            return -jacob_symbol(bmoda, a)
        else:
            print(f"jaco({bmoda}, {a}) \n")
            return jacob_symbol(bmoda, a)
    else:
        bmod8 = b % 8
        newa = a / 2
        print(f"even ----- a/2 = {newa} ----- {b} mod 8 = {bmod8}")
        if bmod8 == 1 or bmod8 == b-1:
            print(f"jaco({newa}, {b}) \n")
            return jacob_symbol(newa, b)
        else:
            print(f"-jaco({newa}, {b}) \n")
            return -jacob_symbol(newa, b)

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

    l = all_value(args.ID, 262915409)
    print(l)
    for y in l:
        symbol = jacob_symbol(y, 262915409)
        print(symbol, "\n\n")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
