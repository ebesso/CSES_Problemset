t = int(input())

for _ in range(t):
    r, c = list(map(int, input().split()))
    if r > c:
        if r % 2 == 0:
            print(r**2 - c + 1)
        else:
            print((r - 1)**2 + c)
    else:
        if c % 2 == 1:
            print(c**2 - r + 1)
        else:
            print((c - 1)**2 + r)


