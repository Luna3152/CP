n = int(input())
a = []

for i in range(n):
    a.append(int(input()) - 1)

node = 0
count = 0

while not node == 1:
    node = a[node]
    count += 1

    if count >= n:
        count = -1
        break

print(count)
