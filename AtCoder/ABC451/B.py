N, M = map(int, input().split())
A = [0] * N
B = [0] * N

beforeNum = [0] * M
afterNum = [0] * M

for i in range(N):
    A[i], B[i] = map(int, input().split())

for j in range(M):
    print(B.count(j + 1) - A.count(j + 1))
