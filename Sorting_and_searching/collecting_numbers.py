n = int(input())
x = list(map(int, input().split()))

lookup = [0] * (n + 1)

for i in range(n):
    lookup[x[i]] = i 

out = 1

for i in range(n):
    if x[i] > 1:
        if lookup[x[i] - 1] > lookup[x[i]]:
            out += 1

print(out)