A1 = [int(x) for x in input().split()]
A2 = [int(x) for x in input().split()]
A3 = [int(x) for x in input().split()]

p456 = (A1.count(4) * A2.count(5) * A3.count(6)) / 6**3
p465 = (A1.count(4) * A2.count(6) * A3.count(5)) / 6**3
p546 = (A1.count(5) * A2.count(4) * A3.count(6)) / 6**3
p564 = (A1.count(5) * A2.count(6) * A3.count(4)) / 6**3
p645 = (A1.count(6) * A2.count(4) * A3.count(5)) / 6**3
p654 = (A1.count(6) * A2.count(5) * A3.count(4)) / 6**3

print(p456 + p465 + p546 + p564 + p645 + p654)
