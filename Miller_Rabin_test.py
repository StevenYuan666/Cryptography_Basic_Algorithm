import random

def miller_rabin(N, k):
    if N != 2 and N % 2 == 0:
        return "multiple of 2, Composite"

    r, u = 0, 0
    while u % 2 == 0:
        r += 1
        u = (N-1)/(2**r)
    u = int(u)
    for _ in range(k):
        a = random.randrange(1, N-1)
        x = pow(a, u, N)
        if x == 1 or x == N-1:
            continue
        else:
            for _ in range(r - 1):
                x = pow(x, 2, N)
                if x != N-1:
                    continue
                if x == N-1:
                    break
            if x != N-1:
                return [a, "Composite"]

    return [a, "Prime"]


if __name__ == '__main__':
    print(miller_rabin(3, 1))
