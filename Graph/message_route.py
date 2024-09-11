from collections import deque

n, m = list(map(int, input().split()))

g = [[] for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, input().split()))

    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

q = deque([0])

prev = [-1 for _ in range(n)]
prev[0] = 0
while len(q) > 0:
    u = q.popleft()
    for e in g[u]:
        if prev[e] == -1:
            prev[e] = u
            q.append(e)

if prev[-1] > -1:
    path = [n]
    c = n - 1
    while c > 0:
        c = prev[c]
        path.append(c + 1)
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))
else:
    print('IMPOSSIBLE')
     


