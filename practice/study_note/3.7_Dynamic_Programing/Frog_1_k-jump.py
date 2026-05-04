n, k = map(int, input().split())
h = [int(x) for x in input().split()]

dp = [0] * n

for i in range(1, n):
    best = float('inf')
    for j in range(1, k + 1):
        if i - j >= 0:
            cost = dp[i - j] + abs(h[i] - h[i - j])
            best = min(best, cost)
    dp[i] = best

print(dp[-1])
