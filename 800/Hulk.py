a = int(input())
print(' that '.join(['I hate' if i %
                     2 == 1 else 'I love' for i in range(1, a+1)]) + ' it')
