N = int(input())
A = [int(x) for x in input().split()]

dp = [0] * (N + 1)
dp[1] = A[0]

for i in range(2, N + 1):
    dp[i] = max(dp[i - 2] + A[i - 1], dp[i - 1])

print(dp[N])
