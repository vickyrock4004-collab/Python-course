#find the sum in a give range

"""for i in range(10):
    print(i + 1)


#Factorial of a give number

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)


#for loop
m = int(input("Enter a number"))

for i in range(1, m): 
        print('9' * i)
print()"""


#fibonacci series

"""a,b = 0,1

for i in range(8):
    print(a)
    a,b =b, a+b"""


#palindrome

'''n = int(input('Enter a number:'))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if(temp == rev):
    print("Palindrome")
else:
    print("Not Palindrome")'''



#increase number using Nested loop

'''rows = int(input('Enter a number'))

num = 1

for i in range(1,rows+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()'''


#print the star

'''rows = int(input('Enter a number'))

for i in range(rows):#0,1,2
    for space in range(i * 2):#0,1*1=1,2*2=4
        print(" ", end="")
    for j in range(2 * (rows - i) - 1):#3-0=3*2 =6-1=5,3-1=2*2=4-1=3,3-2=1*2=2-1=0
        print("*", end=" ")
    print()'''




#print the pyramid number

"""rows = int(input('Enter a number'))

for i in range(1,rows+1):#1,2,3,4
    for space in range(1,(10-i)+1):#10-1=9=9+1=10
        print(end=" ")
    for j in range(1, i +1 ):
        print(j, end='')
    for k in range(i - 1,0,-1):
        print(k, end="")
    print()"""




#print the space 2 pyramid number



'''rows = 5

for i in range(1, rows + 1):#1,2,3,4,5
    for j in range(1, i + 1):#1,12,123,1234,12345
        print(j, end="")
    print(" " * (2 * (rows - i)), end="")#2*5-1=2*4=8,
    for j in range(i, 0, -1):#1,
        print(j, end="")
    print()'''



