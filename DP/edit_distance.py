x = list(input())
y = list(input())

dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

dp[0] = list(range(len(y) + 1))

for i in range(len(x) + 1):
    dp[i][0] = i

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + (0 if x[i - 1] == y[j - 1] else 1))


print(dp[-1][-1])