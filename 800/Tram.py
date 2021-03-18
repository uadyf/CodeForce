n = int(input())
a = [input().split() for i in range(n)]
o = []
x = 0
for i in a:
    x -= int(i[0])
    x += int(i[1])
    o.append(x)
print(max(o))
