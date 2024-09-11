n = int(input())

dp = [0]

for i in range(1, n + 1):
    nums = []
    j = i

    while j > 0:
        if j % 10 > 0:
            nums.append(j % 10)
        j //= 10
    
    shortest = 10**18
    for num in nums:
        shortest = min(shortest, dp[i - num] + 1)
    
    dp.append(shortest)

print(dp[-1])