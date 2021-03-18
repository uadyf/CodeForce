n = int(input())
a = [input().split() for i in range(n)]
o = 0
for i in range(len(a)):
    if i == len(a)-1:
        break
    elif a[i][0][-1] + a[i+1][0][0] == '01' or a[i][0][-1] + a[i+1][0][0] == '10':
        o += 1

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(o)
