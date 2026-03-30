#find the postive or negative number
number = int(input('Enter a Number:'))
if(number > 0):
    print('Postive number:', number)

elif(number < 0):
    print('Negative number:', number)

else:
    print('Enter a valid number')

#even and odd number
num = int(input('Enter a Number:'))

if(num % 2 == 0):
    print('Even number', num)
 
elif(num % 2 != 0):
    print('Odd Number',num)

else:
    print('Enter a valid number')



#Voting task
age = int(input('Enter your age'))

if(age < 18):
    print('your not Eligible', age)

elif((age > 18) and (age < 60)):
    print('your Eligible', age)

elif(age >= 60):
    print('your senior citizen', age)

else:
    print('Enter valid age')


#find the students grade

english_mark = int(input('Enter your English mark: '))
tamil_mark = int(input('Enter your Tamil mark: '))
science_mark = int(input('Enter your Science mark: '))
math_mark = int(input('Enter your Math mark: '))
social_mark = int(input('Enter your Social mark: '))


if(english_mark < 35 or tamil_mark < 35 or science_mark < 35 or 
    math_mark < 35 or social_mark < 35):
    print('Your Grade is "F"')
else:
    total_marks = english_mark + tamil_mark + science_mark + math_mark + social_mark
    average = total_marks / 5

    print('Total marks:', total_marks)
    print('Average:', average)

    if(average >= 90):
        print('Your Grade is "O"')
    elif((average > 80) and (average < 90)):
        print('Your Grade is "A"')
    elif((average > 70) and (average < 80)):
        print('Your Grade is "B"')
    elif((average > 60) and (average < 70)):
        print('Your Grade is "C"')
    elif((average > 45) and (average < 60)):
        print('Your Grade is "D"')
    else:
        print('Your Grade is "E"')








