n = int(input())
a = [list(map(int, input().rstrip().split())) for i in range(n)]
o = 0
for i in a:
    if i[-1] - i[0] >= 2:
        o += 1
print(o)
