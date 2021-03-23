import math
n = int(input())
a = [input().split() for i in range(n)]
q = []
for i in a:
    x = []
    for j in i:
        x.append(int(j))
    q.append(x)

for i in q:
    key = i[0]
    print(min([math.ceil(key/j)*j for j in i[1:]])-key)
