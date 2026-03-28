from heapq import heappop, heappush

# Qの値を格納
q = int(input())

# 追加されるtreeの情報を格納
tree = []

for i in range(q):
    t, h = map(int, input().split())
    if t == 1:
        heappush(tree, h)
    else:
        while tree and tree[0] <= h:
            heappop(tree)
    print(len(tree))
