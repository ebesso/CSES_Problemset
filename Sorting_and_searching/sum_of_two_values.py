from bisect import bisect_left

n, x = list(map(int, input().split()))

a = list(map(int, input().split()))
b = [[a[i], i] for i in range(n)]

b.sort()

impossible = True

for i in range(n):
    j = bisect_left(b, [x - b[i][0], -1])
    if j < n and j != i and b[j][0] == x - b[i][0]:
        print(b[i][1] + 1, b[j][1] + 1)
        impossible = False
        break

if impossible:
    print('IMPOSSIBLE')