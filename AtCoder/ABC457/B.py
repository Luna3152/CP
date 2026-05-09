N = int(input())

LA = []
for i in range(N):
    LA.append(list(map(int, input().split())))

X, Y = map(int, input().split())

print(LA[X - 1][Y])
