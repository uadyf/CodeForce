t = int(input())
for i in range(t):
    a = [int(i) for i in input().split()]
    if a[0] % a[1] == 0:
        print(0)
    else:
        print(a[1]-a[0] % a[1])
