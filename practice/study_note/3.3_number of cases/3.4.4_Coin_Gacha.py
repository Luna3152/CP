N = int(input())

result = 0
for i in range(N):
    result += 1 / (i + 1)
print(N * result)
