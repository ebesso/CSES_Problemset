t = int(input())

while t > 0:
    x, y = list(map(int, input().split()))
    a = min(x, y)
    b = max(x, y)

    k = b - a

    if a == b and a % 3 == 0:
        print('YES')
    elif a - k < 0 or b - k < 0:
        print('NO')
    else:
        if (a - k) % 3 == 0:
            print('YES')
        else:
            print('NO')

    t -= 1

