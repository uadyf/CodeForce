n = [int(i) for i in input().split()]

curr = n[0]
for i in range(n[-1]):
    if str(curr)[-1] != '0':
        curr -= 1
    elif str(curr)[-1] == '0':
        curr = int(str(curr)[:-1])
print(curr)
