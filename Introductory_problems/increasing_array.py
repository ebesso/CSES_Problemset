n = int(input())

x = list(map(int, input().split()))

out = 0

for i in range(1, n):
    if x[i] < x[i - 1]:
        out += x[i - 1] - x[i]
        x[i] = x[i - 1]

print(out)
