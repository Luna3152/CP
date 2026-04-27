A = [int(x) for x in input().split()]


def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B

    if A >= 1:
        return A
    return B


gcd = A[0]

for i in range(1,len(A)):
    gcd = GCD(gcd, A[i])

print(gcd)
