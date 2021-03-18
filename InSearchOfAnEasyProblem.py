n = int(input())
a = input().split()
print('HARD') if all([False for i in a if i == '1']
                     ) == False else print('EASY')
