s = str(input())
start_i = 0
ans = 0

for i, c in enumerate(s):
    if i + 1 == len(s) or s[i + 1] == c:
        ans += (i - start_i + 1) * (i - start_i + 2) // 2
        start_i = i + 1

print(ans % 998244353)
