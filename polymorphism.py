#Same interface → different behavior

class Car:
  def moveForward(self):
    print('Moving')

  def moveForward(self,speed):
    print(speed)



class Summation:

  '''
  #other programming language
  //MethodOverloading -- compile time polymorphism
  int sum(int a, int b):
    return a+b

  float sum(float a, float b):
    return a+b

  int sum(int a, int b, int c):
    return a+b+c  
  sum(1,2)
  sum(1,2,3)
  sum(1.0,5.0)
  '''


 
  def sum(self, *args):
    ans = 0
    for i in args:
      ans +=i
    return ans
  
sum = Summation()
print(sum.sum(1,2,3,4,5,6))



#Method Overriding   

class Father:
  def __init__(self):
    print('Father Constructor')
  def say_hello(self):
    print('Hello from father!')

class Child(Father):
  def __init__(self):
    print('Child Constructor')
  def say_hello(self, name):
    print('Hello from child!',name)


child = Child()
child.say_hello('Vignesh')




