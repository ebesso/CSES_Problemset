from collections import deque

n, m = list(map(int, input().split()))

g = []

for _ in range(n):
    g.extend(list(input()))

monster_distance = [10**18] * n * m
human_distance = [-1] * n * m
monsters = []
human = 0

for i in range(n*m):
    if g[i] == 'M':
        monsters.append(i)
        monster_distance[i] = 0
    elif g[i] == 'A':
        human = i
        human_distance[i] = 0

q = deque(monsters)

while len(q) > 0:
    u = q.popleft()
    
    if u - m > -1:
        if monster_distance[u - m] == 10**18 and g[u - m] == '.':
            q.append(u - m)
            monster_distance[u - m] = monster_distance[u] + 1
    if u + m < m*n:
        if monster_distance[u + m] == 10**18 and g[u + m] == '.':
            q.append(u + m)
            monster_distance[u + m] = monster_distance[u] + 1
    if u % m > 0:
        if monster_distance[u - 1] == 10**18 and g[u - 1] == '.':
            q.append(u - 1)
            monster_distance[u - 1] = monster_distance[u] + 1
    if u % m < m - 1:
        if monster_distance[u + 1] == 10**18 and g[u + 1] == '.':
            q.append(u + 1)
            monster_distance[u + 1] = monster_distance[u] + 1

q = deque([human])
prev = [-1 for _ in range(n * m)]

boundary_position = -1

while len(q) > 0:
    u = q.popleft()
    if human_distance[u] < monster_distance[u]:
        if u < m or u % m == m - 1 or u % m == 0 or u > n*m - m:
            boundary_position = u
        if u - m > -1 and g[u - m] == '.':
            if human_distance[u - m] == -1:
                q.append(u - m)
                human_distance[u - m] = human_distance[u] + 1
                prev[u - m] = u
        if u + m < m*n:
            if human_distance[u + m] == -1 and g[u + m] == '.':
                q.append(u + m)
                human_distance[u + m] = human_distance[u] + 1
                prev[u + m] = u
        if u % m > 0:
            if human_distance[u - 1] == -1 and g[u - 1] == '.':
                q.append(u - 1)
                human_distance[u - 1] = human_distance[u] + 1
                prev[u - 1] = u
        if u % m < m - 1:
            if human_distance[u + 1] == -1 and g[u + 1] == '.':
                q.append(u + 1)
                human_distance[u + 1] = human_distance[u] + 1
                prev[u + 1] = u

if boundary_position > -1:
    print('YES')
    u = boundary_position
    path = []
    while u != human:
        if prev[u] % m == u % m:
            if u > prev[u]:
                path.append('D')
            else:
                path.append('U')
        else:
            if u > prev[u]:
                path.append('R')
            else:
                path.append('L')
        u = prev[u]
    print(len(path))
    path.reverse()
    print(''.join(path))
else:
    print('NO')








