n, x = list(map(int, input().split()))
coins = list(map(int, input().split()))

dp = [-1] * (x + 1)

dp[0] = 0

for i in range(x):
    if dp[i] > -1:
        for c in coins:
            if i + c <= x:
                if dp[i + c] == -1:
                    dp[i + c] = dp[i] + 1
                else:
                    dp[i + c] = min(dp[i + c], dp[i] + 1) % (10**9 + 7)

print(dp[-1])
                
