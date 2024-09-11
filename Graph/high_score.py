#Bellman-Ford algorithm

from collections import deque

n, m = list(map(int, input().split()))

path = [-10**18] * n
path[0] = 0

edges = []
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, x = list(map(int, input().split()))
    g[a - 1].append(b - 1)
    edges.append((a - 1, b - 1, x))

edges.sort()    

for _ in range(n - 1):
    for u, v, c in edges:
        if path[u] > -10**18:
            path[v] = max(path[v], path[u] + c)


positive_cycle_exists = False

for u, v, c in edges:
    if path[u] > -10**18:
        if path[u] + c > path[v]:
            q = deque([v])
            v = [False]*n

            while len(q) > 0:
                u = q.popleft()
                v[u] = True
                if u == n - 1:
                    positive_cycle_exists = True
                    break    
                for e in g[u]:
                    if not v[e]:
                        q.append(e)
                                
if positive_cycle_exists:
    print(-1)
else:
    print(path[-1])