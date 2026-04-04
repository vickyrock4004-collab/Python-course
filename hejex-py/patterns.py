rows = 6

#star ***** pattern
"""for i in range(1,rows+1):
    for j in range(rows-1):
        print('*',end='')
    print()"""

#number 11111 pattern

"""for i in range(1,rows):
    for j in range(rows-1):
        print(i,end='')
    print()"""



#star * and ** pattern

'''for i in range(1,rows):#1
    for j in range(i):
        print('*',end='')
    print()'''

#number 1 and 12 pattern

"""for i in range(1,rows):
    for j in range(1,i+1):
        print(j,end='')
    print()"""

#number 1 and 01,101,0101 pattern

'''for i in range(1,rows+1):
    num = i % 2
    for j in range(1,i+1):
        print(num,end='')
        num = 1-num
    print()'''



#number 1 and 23 pattern

''''num = 1

for i in range(1,rows):#1,2,3,4,5
    
    for j in range(1,i+1):#
        print(num,end=' ')#1,add =1,add =3,add=6,add = 10
        num += 1        
    print()'''


#star ***** pattern
'''for i in range(1,rows+1):
    for j in range(rows,i,-1):
        print('*',end='')
    print()'''


# number 55555 pattern
"""
for i in range(rows,1,-1):
    for j in range(i):
        print(i, end=' ')
    print()"""


#number 11111 pattern

"""for i in range(1,rows):
    for j in range(rows-i+1):
        print(i,end='')
    print()"""

#NUMBER 54321 pattern

'''for i in range(rows):
    for j in range(5,i,-1):
        print(j,end='')
    print()'''
