n = int(input())

if n == 2 or n == 3:
    print('NO SOLUTION')
else:
    out = []
    i = 1
    while i*2 <= n:
        out.append(i*2)
        i += 1
    i = 0
    while 2*i + 1 <= n:
        out.append(2*i + 1)
        i += 1 
    print(' '.join(map(str, out)))

