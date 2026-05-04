N = int(input())
h = [int(x) for x in input().split()]

if N == 1:
    print(0)
    exit()

dp = []
dp.append(0)
dp.append(abs(h[0] - h[1]))

for i in range(2, N):
    dp.append(min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2])))

print(dp[-1])
