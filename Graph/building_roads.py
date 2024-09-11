from collections import deque


n, m = list(map(int, input().split()))

g = [[] for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)


visited = [False] * n

components = []

for i in range(n):
    if not visited[i]:
        components.append(i)
        q = deque([i])

        while len(q) > 0:
            j = q.popleft()
            visited[j] = True
            for e in g[j]:
                if not visited[e]:
                    q.append(e)

print(len(components) - 1)

for i in range(1, len(components)):
    print(components[0] + 1, components[i] + 1)