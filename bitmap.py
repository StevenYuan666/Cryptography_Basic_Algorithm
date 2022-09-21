def bitmap(s: int):
    x = s
    bitmap = [[0 for _ in range(256)] for _ in range(256)]
    for i in range(256):
        for j in range(256):
            bitmap[i][j] = x % 2
            x = x ** 2 % 262915409
    print(bitmap)
            
            
if __name__ == '__main__':
    bitmap(260921269)
