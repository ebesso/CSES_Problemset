#Topsort

import sys

sys.setrecursionlimit(10**5)

n, m = list(map(int, input().split()))

g = [[] for _ in range(n)]

for _ in range(m):
    u, v = list(map(int, input().split()))
    g[u - 1].append(v - 1)

seen = [False] * n
top_sort = []

impossible = False
rec_stack = [False] * n

def dfs(u):
    seen[u] = True
    rec_stack[u] = True

    for e in g[u]:
        if not seen[e]:
            if dfs(e):
                return True
        elif rec_stack[e]:
            return True
    
    top_sort.append(u + 1)
    rec_stack[u] = False
    return False

impossible = False

for i in range(n):
    if not seen[i]:
        if dfs(i):
            impossible = True
            break

if not impossible:
    top_sort.reverse()
    print(' '.join(map(str, top_sort)))
else:
    print('IMPOSSIBLE')



