n, q = list(map(int, input().split()))

x = list(map(int, input().split()))

queries = []

for _ in range(q):
    a, b = list(map(int, input().split()))
    queries.append([a, b])

pre = [0]

for i in range(n):
    pre.append(pre[-1] + x[i])

for i in range(q):
    a, b = queries[i]

    print(pre[b] - pre[a - 1])
    
