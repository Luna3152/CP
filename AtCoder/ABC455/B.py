h, w = map(int, input().split())
s = [0] * h
for i in range(h):
    s[i] = list(str(input()))

hw_list = [
    [i, j, k, l]
    for i in range(h)
    for j in range(i, h)
    for k in range(w)
    for l in range(k, w)
]

count = 0

for element in hw_list:
    found = False
    ij_count = 0
    for i in range(element[0], element[1] + 1):
        for j in range(element[2], element[3] + 1):
            if s[i][j] == s[element[0] + element[1] - i][element[2] + element[3] - j]:
                ij_count += 1

    if ij_count == (element[1] + 1 - element[0]) * (element[3] + 1 - element[2]):
        count += 1

print(count)
