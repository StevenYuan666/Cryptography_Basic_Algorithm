from matplotlib import pyplot as plt


def bitmap(s: int):
    x = s
    bitmap = [[0 for _ in range(256)] for _ in range(256)]
    for i in range(256):
        for j in range(256):
            bitmap[i][j] = x % 2
            x = x ** 2 % 262915409
    plt.imshow(bitmap)
    plt.show()


if __name__ == '__main__':
    bitmap(260921269)
