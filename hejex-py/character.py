#increasig trinagle A and BB

'''n = 5

p =65

for i in range(n):
    for j in range(i+1):
        print(chr(p),end=' ')
    p+=1
    print()'''

#method 2

'''n = 5

for i in range(n):
    print((chr(65 + i) + ' ') * (i + 1))'''

#incrcreasing triangle A and AB

'''n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=' ')
    print()'''

#continue letter across rows
'''n = 5
ch = 65

for i in range(1,n):
    for j in range(i):
        print(chr(ch),end=' ')
        ch += 1
    print()'''


#letter pattern A and BA and CBA

'''n =5


for i in range(n):
    for j in range(i,-1,-1):
        print(chr(65 + j),end=' ')
    print()'''



