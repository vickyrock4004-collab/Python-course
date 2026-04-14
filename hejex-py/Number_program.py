#reserve method

'''n = 268
m = n
rev = 0
while m != 0:
    d = m%10
    m = m//10
    print(d)'''


#palindrome

"""n = 121
m = n
rev = 0

while(m != 0):
    d = m%10
    rev = rev * 10 + d
    m = m//10

if(rev == n):
    print('Number is palindrome:',rev)

else:
    print('Number is not palindrome',rev)"""

"""
pass 1
 d= 268%10=8
 rev = 0 * 10 + 8 =8
 m = 268//10 =26

 pass 2

 d= 26%10=6
 rev = 8*10+6 = 80+6=86
 m = 26//10 = 2

 pass 3
 d = 2%10 =2
 rev = 86*10+2=860+2=862
 m = 2//10=0

"""

#add 123=1+2+3=6
'''num = 121
total = 0

for digit in str(num): 
    total += int(digit) 

print(total)'''

#spy number

'''num = 1124

sum_digits = 0
product = 1

for digit in str(num):
    sum_digits += int(digit)
    product *= int(digit)

if sum_digits == product:
    print("Spy Number:",sum_digits,product)
else:
    print("Not a Spy Number:",sum_digits,product)'''

#Niven Number(add and module)

'''num = 18

digit_sum = 0

for digit in str(1,100):
    digit_sum += int(digit)

if digit % digit_sum == 0:
    print("Niven Number:",digit_sum)
else:
    print("Not Niven Number:",digit_sum)'''


for num in range(1, 101):
    digit_sum = 0

    for digit in str(num):
        digit_sum += int(digit)

    if num % digit_sum == 0:
        print(num, end=' ')


