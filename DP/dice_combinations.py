n, x = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [10**18] * (x + 1)
seen = [False] * (x + 1)

for i in c:
    if i <= x:
        seen[i] = True
        dp[i] = 1

for i in range(0, x):
    if seen[i]:
        for j in range(len(c)):
            if i + c[j] <= x: 
                dp[i + c[j]] = min(dp[i + c[j]], dp[i] + 1) % (10**9 + 7)
                seen[i + c[j]] = True
if seen[-1]:    
    print(dp[-1])
else:
    print(-1)

