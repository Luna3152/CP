N, K = map(int, input().split())

LA = []
for i in range(N):
    LA.append(list(map(int, input().split())))

C = [int(x) for x in input().split()]

A = []
for i in range(N):
    A.append(LA[i][1:])

B = []
for i in range(N):
    B.append([A[i], C[i]])

countList = []
count = 0
for i in range(N):
    count += len(B[i][0]) * B[i][1]
    countList.append(count)
    if count >= K:
        if len(countList) == 1:
            initial = countList[-1] + 1
            modulo_K = K % len(B[i][0])
            for j in range(len(B[i][0]) * B[i][1]):
                if modulo_K == j + countList[-1] % len(B[i][0]):
                    print(B[i][0][j + countList[-1] % len(B[i][0]) - 1])
                    exit()
        else:
            initial = countList[-2] + 1
            modulo_K = K % len(B[i][0])
            for j in range(len(B[i][0]) * B[i][1]):
                if modulo_K == j + countList[-2] % len(B[i][0]):
                    print(B[i][0][j + countList[-2] % len(B[i][0]) - 1])
                    exit()
