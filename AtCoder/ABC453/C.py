n = int(input())
l = [int(x) for x in input().split()]

before_moved = 0.5
count = 0

for i in range(len(l)):
    if before_moved < 0:
        after_moved = before_moved + l[i]
        if before_moved * after_moved < 0:
            count += 1
        before_moved = after_moved
    elif before_moved > 0:
        after_moved = before_moved - l[i]
        if before_moved * after_moved < 0:
            count += 1
        before_moved = after_moved

print(count)
