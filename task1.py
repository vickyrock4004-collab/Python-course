#user input

"""num = int(input('Enter the vaule of num:'))
print(num + 5)"""

#Average of marks

"""mark1 = float(input('Enter mark1:'))
mark2 = float(input('Enter mark2:'))
mark3 = float(input('Enter mark3:'))

totalmark = mark1 + mark2 + mark3

Averagemark = totalmark / 3

print(Averagemark)"""

#Expression
#3a2 + b -2c

'''a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

val = 3*(a ** 2) + b - (2*c)

print(val)'''


#Unit Digit

'''num = int(input())

"""print(num[len(num) - 1])"""
print(num[-1])
print(num % 10)'''

#Tenth Digit
#11859

"""num = int(input('Enter number:'))
num //= 10

print(num % 10)"""

#conditional statement

'''if (5 > 5):
  print('5 is equal to 5')
  print('program successful')

print('not error')'''

"""num = int(input('Enter number:'))

if (num > 0):
  print('postive number')
  print(num, 'is positive number')

elif (num == 0):
  print('Zero')

else :
  print('Negative number')
  print(num, 'is negative number')"""

'''x = 5
y = 10
if x > y:
  largest = x

else:
  largest = y

print("The largest number is:", largest)'''

'''a = 5

if(a > 1):
  print('a greater than 1')

elif(a == 5):
  print('a is five')'''

#Nested if

'''age = 18
eatpizza = True
exercise = False'''

"""if(age < 30):
  if(eatpizza):
    print('Unfit')
  else:
    print('Fit')

else:
  if(exercise):
    print('Unfit')
  else:
    print('fit')"""

#Ternary Operator

"""print('child'if(age < 18) else 'adult') """

'''print(("Unfit" if(eatpizza) else 'fit') if(age < 30) else ('fit' if(exercise) else 'unfit'))'''


#odd or Even

'''num = int(input('Enter Number:'))'''

'''if(num % 2 == 0):
  print(num, 'is a even number')

elif(num % 2 != 0):
  print(num, 'is a odd number')

else:
  print('Enter a correct number')'''

'''print('Even' if(num % 2 == 0) else 'odd')'''

#Iterative Statement

# forloop

'''num = 5

for i in range(100, 50, -1):
  print(i)'''

'''for i in range(5,11,2):
  print(i, end="")'''

#while

"""num = 5

while(num > 0):
  print('vignesh')
  num -= 1"""

'''count = 0
while (count < 10):
  print(count)
  count += 1'''

#Pass Statement (empty Statement)

"""if 5 == 5:
  pass"""

#jump statement

"""for i in range(1, 11):
  if i == 5:
    continue
  print(i)"""


#Nested loop

n = int(input("Enter n:"))

"""for j in range(n):
  for i in range(1, j+1):
    print(i, end=' ')
  print()"""
