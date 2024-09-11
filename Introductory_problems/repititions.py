x = list(input())

c = 1
best = 1

for i in range(1, len(x)):
    if x[i] == x[i - 1]:
        c += 1
    else:
        c = 1
    best = max(best, c)
print(best)
