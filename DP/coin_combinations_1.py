n, x = list(map(int, input().split()))
coins = list(map(int, input().split()))

dp = [0] * (x + 1)

dp[0] = 1

for i in range(x):
    if dp[i] > 0:
        for c in coins:
            if i + c <= x:
                dp[i + c] += dp[i]
                dp[i + c] %= (10**9 + 7)
                

print(dp[-1])
                
