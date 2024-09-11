import bisect

n = int(input())
x = list(map(int, input().split()))

towers = []

for i in x:
    pos = bisect.bisect_right(towers, i)
    if pos == len(towers):
        towers.append(i)
    else:
        towers[pos] = i

print(len(towers))