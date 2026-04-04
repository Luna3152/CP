h, w = map(int, input().split())

wb_list = [0] * w

print("#" * w)
for i in range(h - 2):
    for j in range(w):
        if j == 0 or j == w - 1:
            wb_list[j] = "#"
        else:
            wb_list[j] = "."
    print(*wb_list, sep="")

print("#" * w)
