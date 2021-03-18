n = int(input())
x = [str(input()) for i in range(n)]

for i in x:
    if len(i) <= 10:
        print(i)
    else:
        o = i[0] + str(len(i[1:-2])+1) + i[-1]
        print(o)