import re

n = [int(j) for j in input().split(' ')]
a = [int(i) for i in input().split(' ')]
limit = n[-1]
if a.count(0) == len(a):
    print('0')
else:
    for i in range(n[0]-n[-1]):
        if n[limit+i] > limit:
            continue
        elif n[limit+i] < limit:
            n