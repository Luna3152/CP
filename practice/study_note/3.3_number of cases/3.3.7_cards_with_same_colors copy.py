N = int(input())
A = [int(x) for x in input().split()]

count = [0] * N

for x in A:
    count[x - 1] += 1

result = 0
for c in count:
    result += c * (c - 1) // 2

print(result)
