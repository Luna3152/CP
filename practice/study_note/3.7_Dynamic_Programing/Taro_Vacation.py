N = int(input())
A = [int(x) for x in input().split()]

dp = [[0] * 2 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = dp[i - 1][0] + A[i - 1]

print(max(dp[N]))
