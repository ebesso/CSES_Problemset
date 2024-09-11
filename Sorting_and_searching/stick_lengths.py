#Special binary search

n = int(input())

p = list(map(int, input().split()))

def get_cost(l):
    out = 0
    for i in range(n):
        out += abs(p[i] - l)
    
    return out

best = -1
i = 10**9
x = -1
while i > 0:
    while get_cost(x + i) > get_cost(x + i + 1):
        x += i
    i //= 2

print(get_cost(x + 1))