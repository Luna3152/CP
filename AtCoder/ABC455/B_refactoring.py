h, w = map(int, input().split())
s = [input() for _ in range(h)]

count = 0

for h1 in range(h):
    for h2 in range(h1, h):
        for w1 in range(w):
            for w2 in range(w1, w):
                ok = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        if s[i][j] != s[h1 + h2 - i][w1 + w2 - j]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    count += 1

print(count)
