a = input()
b = input()
o = ''
for i, j in zip(a, b):
    if i != j:
        o += '1'
    else:
        o += '0'
print(o)
