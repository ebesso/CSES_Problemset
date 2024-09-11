#Dijkstra

import heapq

n, m = list(map(int, input().split()))

g = [[] for _ in range(n)]

for _ in range(m):
    u, v, c = list(map(int, input().split()))
    g[u - 1].append((v - 1, c))

q = []
distance = [10**18 for _ in range(n)]
distance[0] = 0

heapq.heappush(q, (0, 0))

visited = [False] * n

while len(q) > 0:
    d, u = heapq.heappop(q)

    if not visited[u]:
        visited[u] = True
        
        for e, c in g[u]:
            if distance[u] + c < distance[e]:
                distance[e] = distance[u] + c
                heapq.heappush(q, (distance[e], e))

print(' '.join(map(str, distance)))
