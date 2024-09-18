n = int(input())

fives = 0
j = 5
while j <= n:
    fives += n // j
    j *= 5

print(fives)
