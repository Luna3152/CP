n, a, b = map(int, input().split())
s = list(str(input()))

count = 0
count_b = 0

for i in s:
    if i == "a":
        if count < a + b:
            print("Yes")
            count += 1
        else:
            print("No")
    elif i == "b":
        count_b += 1
        if count < a + b and count_b <= b:
            print("Yes")
            count += 1
        else:
            print("No")
    else:
        print("No")
