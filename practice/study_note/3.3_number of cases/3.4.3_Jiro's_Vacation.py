N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

result = 0.0
for i in range(N):
    result += 1 * A[i] / 3 + 2 * B[i] / 3

print(result)
