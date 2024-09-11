import bisect

n = int(input())
x = list(map(int, input().split()))
piles = []

for i in range(n):
    idx = bisect.bisect_left(piles, x[i])
    if idx == len(piles):
        piles.append(x[i])
    else:
        piles[idx] = x[i]