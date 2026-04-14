#square pattern
'''n = 5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()'''

#increasing Trianble pattern

'''n = 5

for i in range(1,n):
    for j in range(i):
        print('*',end=' ')
    print()'''
#decreasing Triangle pattern
'''n = 5

for i in range(n):
    for j in range(i,n):
        print('*', end=' ')
    print()'''

#increasing right sided Triangle pattern

'''n = 5

for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()'''

#decreasing right sided Triangle pattern

'''n = 5

for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('*',end=' ')
    print()'''
#2-method
'''n = 5

for i in range(n):
    print(' ' * (n-i-1) + '*' * (i+1))'''
   
#Hill pattern

'''n = 5

for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    for l in range(i):
        print('*',end=' ')
    print()'''

#2-method

'''n =5

for i in range(n):
    print('  '*(n-i),end=' ')
    print('* ' * (2 * i+ 1))'''
    


#Reverse Hill pattern

'''n = 5

for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('*',end=' ')
    for l in range(i,n):
        print('*',end=' ')
    print()'''

#2-method

'''n = 5

for i in range(n):
    print('  ' * i, end='')
    print('* ' * (2 * (n - i) - 1))'''

#diamond Pattern
"""
n = 5

for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    for l in range(i):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(i,n-1):
        print('*',end=' ')
    for l in range(i,n):
        print('*',end=' ')
    print()"""

#2-method

'''n = 5

# Top
for i in range(n):
    print('  ' * (n - i), end='')
    print('* ' * (2 * i + 1))

# Bottom
for i in range(n - 1):
    print('  ' * (i + 2), end='')
    print('* ' * (2 * (n - i - 2) + 1))'''
        

#unique pattern section

#square space pattern

'''rows = 5

for i in range(rows):
    for j in range(rows):
        if(i == j or i+j == rows-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()'''
    
    
