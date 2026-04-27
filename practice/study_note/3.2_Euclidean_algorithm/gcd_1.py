A, B = map(int, input().split())


def GCD(A, B):
    while A >= 1 and B >= 1:
        if A < B:
            B = B % A
        else:
            A = A % B

    if A >= 1:
        return A
    return B


print(GCD(A, B))
