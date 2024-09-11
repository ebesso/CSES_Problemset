#1D arrays are faster

from collections import deque

n, m = list(map(int, input().split()))
g = []

for i in range(n):
    g.extend(list(input()))

visited = [False for _ in range(n*m)]

found = False

paths = ['' for _ in range(n*m)]
b_coordinate = 0
for i in range(n*m):
    if g[i] == 'A':
        q = deque([i])

        while len(q) > 0:
            pos = q.popleft()

            if g[pos] == 'B':
                found = True
                b_coordinate = pos
                break
                

            directions = [(pos + m, 'D'), (pos - m, 'U'), (pos + 1, 'R'), (pos - 1, 'L')]
            for direction in directions:
                new_pos, turn = direction
                if new_pos > -1 and new_pos < n*m and not visited[new_pos] and (g[new_pos] == '.' or g[new_pos] == 'B'):
                    if (turn == 'R' and new_pos % m == 0) or (turn == 'L' and new_pos % m == m - 1):
                        pass
                    else:
                        q.append(new_pos)
                        visited[new_pos] = True
                        paths[new_pos] = turn
    if found:
        break

if not found:
    print('NO')
else:
    print('YES')
    path = []
    pos = b_coordinate
    while g[pos] != 'A':
        turn = paths[pos]
        path.append(turn)
        if turn == 'U':
            pos += m
        elif turn == 'D':
            pos -= m
        elif turn == 'L':
            pos += 1
        elif turn == 'R':
            pos -= 1
    path.reverse()
    print(len(path))
    print(''.join(path))