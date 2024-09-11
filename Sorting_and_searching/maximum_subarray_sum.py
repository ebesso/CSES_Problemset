n = int(input())

x = list(map(int, input().split()))

current = x[0]
best = x[0]

for i in range(1, n):
    current = max(current + x[i], x[i])
    best = max(best, current)

print(best)