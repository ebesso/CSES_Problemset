n = int(input())
arrive = []
leave = []

for i in range(n):
    a, b = list(map(int, input().split()))
    arrive.append(a)
    leave.append(b)

arrive.sort()
leave.sort()

result = [2*n]

i, j = 0, 0

current, best = 0, 0

while i < n and j < n:
    if arrive[i] < leave[j]:
        current += 1
        i += 1
    else:
        current -= 1
        j += 1
    
    best = max(best, current)

print(best)