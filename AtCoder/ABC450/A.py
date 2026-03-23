N = int(input())
l = []

for i in range(N, 0, -1):
    l.append(i)

print(*l, sep=",")
