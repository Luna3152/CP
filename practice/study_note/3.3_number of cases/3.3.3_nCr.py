n, r = map(int, input().split())
r = min(r, n - r)

res = 1
for i in range(1, r + 1):
    res = res * (n - r + i) // i

print(res)
