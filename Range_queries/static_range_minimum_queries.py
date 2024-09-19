#Sparse table
from collections import *
from itertools import permutations #No repeated elements
import sys, math
sys.setrecursionlimit(10**5)
itr = (line for line in sys.stdin.read().split('\n'))
INP = lambda: next(itr)
def ni(): return int(INP())
def nl(): return [int(_) for _ in INP().split()]
def err(*s): print(*s, file=sys.stderr)

n, q = nl() 

x = nl() 

queries = []

for _ in range(q):
    a, b = nl()
    queries.append([a, b])

k = int(math.log2(n))

lookup = [[0 for _ in range(k + 1)] for _ in range(n)]

for i in range(n):
    lookup[i][0] = x[i]

for j in range(1, k + 1):
    i = 0
    while i + (1 << j) < n + 1:
        lookup[i][j] = min(lookup[i][j - 1], lookup[i  + (1 << (j - 1))][j - 1])
        i += 1

for i in range(q):
    a, b = queries[i] 
    a -= 1
    b -= 1
    j = int(math.log2(b - a + 1))
    print(min(lookup[a][j], lookup[b - (1 << (j)) + 1][j]))
