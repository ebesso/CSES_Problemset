n = int(input())

set_1 = []
set_2 = []
total = n / 2 * (n + 1)

if total % 2 == 1:
    print('NO')
else:
    current = total // 2
    i = n
    while i > 0:
        if current >= i:
            set_1.append(i)
            current -= i
        else:
            set_2.append(i)
        i -= 1
    if current == 0:
        print('YES')
        print(len(set_1))
        print(' '.join(map(str, set_1)))
        print(len(set_2))
        print(' '.join(map(str, set_2)))




