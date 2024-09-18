n = int(input())

current = 1

for i in range(1, n + 1):
    current *= 2
    current %= 10**9 + 7

print(current)
    
