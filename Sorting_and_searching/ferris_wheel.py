n, x = list(map(int, input().split()))
p = list(map(int, input().split()))

p.sort()

i, j = 0, n - 1
count = 0

while i <= j:
    if p[i] + p[j] <= x:
        count += 1
        i += 1
        j -= 1
    else:
        j -= 1
        count += 1

print(count)