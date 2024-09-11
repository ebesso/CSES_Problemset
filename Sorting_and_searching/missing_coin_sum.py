n = int(input())
x = list(map(int, input().split()))

x.sort()

a = 0
i = 0

while i < n and x[i] <= a + 1:
    a += x[i]
    i += 1

print(a + 1)


