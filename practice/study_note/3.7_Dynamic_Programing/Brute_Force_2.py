N, S = map(int, input().split())
A = [int(x) for x in input().split()]

dp = [[False] * (S + 1) for _ in range(N + 1)]

dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        if dp[i - 1][j] or (j >= A[i - 1] and dp[i - 1][j - A[i - 1]]):
            dp[i][j] = True

if dp[N][S]:
    print("Yes")
else:
    print("No")
