n = int(input())

dp = []

for i in range(n + 1):
    if i <= 1:
        dp.append(1)
    else:
        dp.append(dp[i - 1] + dp[i - 2])

print(dp[-1])
