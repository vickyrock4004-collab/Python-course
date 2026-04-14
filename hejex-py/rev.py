#reverse Number


'''n = 321 #32,3 , 0
rev = 0 # 1, 12 123

while(n > 0): #321 > 0 T, 32 > 0 T, 2 > 0 T
    digit = n % 10 #321 % 10 =1 , 32 % 10 = 3 % 10
    rev = rev * 10 + digit#0*10 + 1 = 1 , 1 * 10 + 2 = 10+1 = 12, 12 * 10 + 3 = 120 +3 = 123
    n = n // 10 #321 // 10 = 32, 32 // 10 = 3 // 10

print(rev)'''


#Add the each number    
'''num = 121
total = 0

for digit in str(num): #"121"
    total += int(digit) #0+1 = 1+2 =3+1 =4

print(total)'''



#find the second Largest Number

''''lst = [10,45,32,67,89,23]

largest = 0

second = 0

for i in range(len(lst):#10
    if(lst[i] > largest):#10>0 =T, 45 > 10 = T, 32 > 45 =F , 67 > 45 = T, 89 > 67 =  T 23 > 89 =F
        second = largest#s=0, s=10 s =45 s =67
        largest = lst[i]#l=10, l = 45, l = 67 l = 89

    elif(lst[i] > second and lst[i] < largest):# 32 > 10 T and 32 < 45 T, 23 > 67 F and 23 < 89 F
        second = lst[i]#32


print('Second Largest:', second)'''



#find the odd and even number

'''lst = [11,22,33,44,55,66]

even = []

odd = []

for i in range(len(lst)):
    if(lst[i] % 2 == 0):
        even.append(lst[i])

    #elif(lst[i] != 0):
    else:
        odd.append(lst[i])


print('Even Number:',even)
print('Odd Number:',odd)'''

#find squares list

'''square_List = []

for squ in range(1,21):
    square_List.append(squ**2)
    #a = squ * squ
    #square_List.append(a)


print('Square List:',square_List)'''

#Rotation List(Left/Right)

"""lst = [1, 2, 3, 4, 5]

rot = input('Enter rotation (left/right): ')
number = int(input("Enter number of rotations: "))

number = number % len(lst)#2 % 5 = 2

if(rot == "left"):
    lst = lst[number:] + lst[:number] #lst[2:]=[3,4,5] + lst[:2] = [1,2]
else:
    lst = lst[-number:] + lst[:-number]

print("Rotated List:", lst)"""


#find the leap year or not

'''year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
    print(year,"is a leap year.")
else:
    print(year, "is not a leap year.")'''




#print prime number


"""for num in range(2, 101):
    prime = 1

    for i in range(2, num):
        if(num % i == 0):
            prime = 0
            break
            
    if(prime):
        print(num, end=" ")"""


#recursion function

'''def factorcial(n):
  if(n == 0):
    return 1
  
  else:
    return n * factorcial(n-1)
  
result = factorcial(5)

print(result)'''

# Using the function find sum and average

'''def number():
    lst = [22,33,44,55,66]

    total = 0

    for num in lst:
        total += num
        
    average = total / len(lst)

    return total,average

print(number())'''


#Pascal's Triangle pattern

"""rows = 5

for i in range(rows):
    print(" " * (rows - i), end="")

    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()"""

#Pattern

rows = 5

'''for i in range(1, rows+1):
    for j in range(1,i+1):
        print(j, end="")

    print()'''

'''for i in range(1, rows+1):
    for j in range(1,i+1):
        print(i , end='')
    print()'''





'''for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()'''
        

'''for i in range(rows):#0,1,2,3,4
    for j in range(i+1):#1
        print(' ', end="")
    for k in range(2*(rows - i)-1):#2*5-0 = 10-1=9,2*5-1=2*4=
        print('*',end='')

    print()'''


'''for i in range(1,5+1):
    for j in range(1,i+1):
        print(j,end='')
    print()'''

""""for i in range(1,rows+1):#1,2,3,4,5
    for j in range(1,i+1):#1,2=1,1,3=22
        print(i,end="")

    print()"""

'''for i in range(rows):#0,1,2,3,4
    for j in range(rows,rows-i-1,-1):#5,4,-1=5,5,
        print(j,end='')
    print()'''
 

'''for i in range(4):
    if(i % 2 == 0):
        continue
        
    print(i*i if(i>1) else i+2, end=' ')'''

'''s = "Hello 123#"

letters = digits = spaces = special = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch == ' ':
        spaces += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special:", special)'''





    

    
