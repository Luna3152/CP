N = int(input())
A = [int(x) for x in input().split()]

count_100 = 0
count_200 = 0
count_300 = 0
count_400 = 0

for x in A:
    if x == 100:
        count_100 += 1
    elif x == 200:
        count_200 += 1
    elif x == 300:
        count_300 += 1
    else:
        count_400 += 1

print(count_100 * count_400 + count_200 * count_300)
