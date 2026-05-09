N, K = map(int, input().split())
L = []
A = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    L.append(tmp[0])
    A.append(tmp[1:])

C = [int(x) for x in input().split()]

count = 0

for i in range(N):
    total = L[i] * C[i]

    if count + total >= K:
        offset = K - count
        index = (offset - 1) % L[i]
        print(A[i][index])
        exit()
    count += total
