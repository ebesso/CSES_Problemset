#Floyd Warshall
#Python is too slow

n, m, q = list(map(int, input().split()))

adj = [[10**18 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    u, v, c = list(map(int, input().split()))
    adj[u - 1][v - 1] = min(adj[u - 1][v - 1], c)
    adj[v - 1][u - 1] = min(adj[v - 1][u - 1], c)

distance = [[10**18 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            distance[i][j] = 0
        elif adj[i][j] < 10**18:
            distance[i][j] = adj[i][j]
            distance[j][i] = adj[j][i]

for i in range(n):
    for j in range(n):
        for k in range(n):
            distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])



for _ in range(q):
    u, v = list(map(int, input().split()))
    if distance[u - 1][v - 1] < 10**18:
        print(distance[u - 1][v - 1])
    else:
        print(-1)