N = int(input())
A = [int(x) for x in input().split()]

seen = {}
count = 0

for x in A:
    complement = 100000 - x
    count += seen.get(complement, 0)

    seen[x] = seen.get(x, 0) + 1
print(count)
