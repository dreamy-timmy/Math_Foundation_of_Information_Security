# print('7168 7168'.split(', '))

from itertools import combinations

a, b, c = 1, 2, 3
l = []
for k in list(combinations([a,b,c], 1)):
    [l.append(x) for x in k]

# print(l)
# for k in range(3, 0, -1):
#     print(k)


for i in range(23):
    for j in range(10):
        print(j)
        break