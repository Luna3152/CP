n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
mod = 998244353

sum_ai = sum(a[i] * (i + 1) for i in range(n)) % mod
sum_b = sum(b) % mod

term1 = sum_ai * sum_b

s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = (s[i] + a[i]) % mod


term2 = 0
for j in range(1, m + 1):
    if b[j - 1] == 0:
        continue

    inner = 0

    for k in range(1, n // j + 1):
        l = k * j
        r = min((k + 1) * j - 1, n)

        segment_num = (s[r] - s[l - 1]) % mod
        inner = (inner + k * segment_num) % mod

    term2 = (term2 + b[j - 1] * j % mod * inner) % mod

print((term1 - term2) % mod)
