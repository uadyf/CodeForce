import re

n = int(input())
x = [re.sub(r'\s','',input()) for _ in range(n)]

o = 0
for i in x:
    if i.count('1') >= 2:
        o += 1
print(o)