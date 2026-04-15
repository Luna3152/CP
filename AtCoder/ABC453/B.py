t, x = map(int, input().split())
A = [int(x) for x in input().split()]

B = []

for i in range(len(A)):
    if i == 0:
        B.append(A[i])
        print(i, A[i])
    else:
        if abs(A[i] - B[-1]) >= x:
            B.append(A[i])
            print(i, A[i])
