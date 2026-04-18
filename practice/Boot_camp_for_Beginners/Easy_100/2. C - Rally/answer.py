n = input()
x = [int(x) for x in input().split()]
m = 101

result = []

for p in range(1, m):
    cost = 0
    for j in x:
        cost += (j - p) ** 2
    result.append(cost)

print(min(result))
