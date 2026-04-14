
#Round 1 – Basic but revealing
'''a = [1,2,3]
b = a
b = b + [4,5]

print(a)
print(b)'''


#Round 2 – Logic check

'''num = 123 #12,1,0
m = num
rev = 0#3,32

while(num > 0):#123>0=T,12>0=T,1>0=T,0>0=F
    rev = rev * 10 + num % 10#0*10 + 123 % 10 =0+3=3,3*10+12%10=30+2=32,32*10+1%10=320+1=321
    num = num // 10 #123//10=12,12//10=1,1//10=0

print(rev)

if(m == rev):
    print('palindrome:',rev)
else:
    print('Not palindrome:',rev)'''

'''def is_palindrome(num):
    temp = num
    rev = 0

    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10

    return num == rev
print(is_palindrome(121))'''

#square parallel bar pattern
rows=5

'''for i in range(rows):
    for j in range(rows):
        if(j == 0 or j == rows -1):
            print('*',end=' ')
        else:
            print(' ',end)
    print()'''

#square plus pattern

'''for i in range(rows):
    for j in range(rows):
        if(i == rows//2 or j == rows//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#cross pattern

'''for i in range(rows):
    for j in range(rows):
        if(i == j or i+j == rows-1):
        else:
            print(' ',end=' ')
    print()'''


#Hollow square pattern

'''for i in range(rows):#0,1,2
    for j in range(rows):#01234
        if(i == 0 or j == 0 or i == rows - 1 or j == rows - 1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#hollow increasing triangle pattern

'''for i in range(rows):#0
    for j in range(i+1):#
        if(i == rows-1 or j == 0 or j == i):#
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#hollow decreasing triangle pattern


'''for i in range(rows):#0,1,2
    for j in range(rows):#01234
        if(i == 0 or i == j or j == rows-1):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()'''


#triangle pattern


'''for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    for j in range(rows):
        if(i == rows-1 or j == 0 or j == i):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()'''





# N pattern

'''for i in range(rows):#0,
    for j in range(rows):#01234
        if(j == 0 or i==j or j == rows-1):
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()'''
        


#|_| pattern

'''for i in range(rows):
    for j in range(rows):
        if(j == 0 or j == rows-1 or i == rows-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

    
