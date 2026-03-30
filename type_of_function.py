# void function no return the fucntion


'''def add():
  a = int(input('Enter a number'))
  b = int(input('Enter a number'))
  print(a+b)

sum1 = add()
print(sum1)

#unvoid function
def sub():
  a = int(input('Enter a number'))
  b = int(input('Enter a number'))
  return a-b

sum2 = sub()
print(sum2)'''

#Function Arguments

def add(a,b):
  return a+b


def sub(a,b):
  return a-b


def mul(a,b):
  return a*b



def div(a,b):
  return a/b


a = int(input('Enter a number'))
b = int(input('Enter a number'))

sum1 = add(a,b)
sub1 = sub(a,b)
mul1 = mul(a,b)
div1 = div(a,b)

print(sum1, sub1, mul1, div1)

#task

def area_of_rectangle(length, width):
  return length * width



rectangle_area = area_of_rectangle(5,3)
print(rectangle_area)
