n = int(input())
x = list(map(int, input().split()))

seen = set([x[0]])

i = 0
j = 1
out = 1

while j < n:
    if x[j] in seen:
        while x[i] != x[j]:
            seen.remove(x[i])
            i += 1
        i += 1
    else:
        seen.add(x[j])
        out = max(out, j - i + 1)
    j += 1

print(out)