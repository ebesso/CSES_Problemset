n, x = list(map(int, input().split()))
coins = list(map(int, input().split()))

coins.sort()

dp = [0] * (x + 1)
dp[0] = 1

for c in coins:
    for i in range(0, x + 1):
        if dp[i] > 0:
            if i + c <= x:
                dp[i + c] += dp[i]
                dp[i + c] %= 10**9 + 7
            else:
                break
    

print(dp[-1])


