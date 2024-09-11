n, m = list(map(int, input().split()))
g = []

for i in range(n):
    g.append(list(input()))

visited = [[False for _ in range(m)] for _ in range(n)]

rooms = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and g[i][j] == '.':
            q = [(i, j)]
            rooms += 1

            while len(q) > 0:
                r, c = q.pop()
                directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for direction in directions:
                    dr, dc = direction
                    if dr > - 1 and dr < n and dc > -1 and dc < m:
                        if not visited[dr][dc] and g[dr][dc] == '.':
                            q.append((dr, dc))
                            visited[dr][dc] = True
print(rooms)