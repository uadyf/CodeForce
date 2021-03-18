a = input()
if sum(1 for i in a if i.isupper()) > sum(1 for i in a if i.islower()):
    print(a.upper())
else:
    print(a.lower())
