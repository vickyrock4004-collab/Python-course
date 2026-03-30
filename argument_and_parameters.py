'''
keyword Argument
Default Argument
Positional Argument
'''


#positional Argument is first Argument

def area_of_rectangle(length, width): #parameters
  return length * width


#keyword Argument

rectangle_area = area_of_rectangle(5,3) #arguments
print(rectangle_area)


def area_of_rectangle(length, width): #parameters
  return length * width



rectangle_area = area_of_rectangle(length=5, width=3) #arguments
print(rectangle_area)

#Default Argument is last argument

rectangle_area = area_of_rectangle(5,3) #arguments
print(rectangle_area)


def area_of_rectangle(length, width=1): #parameters
  return length * width



rectangle_area = area_of_rectangle(5) #arguments
print(rectangle_area)

#task

def greet(name, message='Hello'):

  print(message, name + '!')

greet('Python')