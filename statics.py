from abc import ABC, abstractmethod 

class Car(ABC):
  @abstractmethod # is called Decorators
  def moveForward(self):
    pass
  
  @abstractmethod
  def moveBackward(self):
    pass

  @abstractmethod
  def fm(self):
    pass

class Swift(Car):

  @staticmethod
  def moveForward():
    print('Swift is moving forward!')
  
  def moveBackward(self):
    print('Swift is moving backward!')

  def fm(self):
    print('Swift is playing fm')



class Innova(Car):
  def moveForward(self):
    print('Innova is moving forward!')
  
  def moveBackward(self):
    print('Innova is moving backward!')

  def fm(self):
    print('Innova is playing fm')

'''swift =Swift()
swift.moveForward()'''

#Swift.moveForward()
#Swift.moveBackward()


#Method Overriding   

class Father:
  age = 0 #Class variable
  def __init__(self):
    self.name = 'Father' #Instance variable
    print('Father Constructor')
  def say_hello(self):
    print('Hello from father!')

class Child(Father):
  def __init__(self):
    print('Child Constructor')
  def say_hello(self, name):
    print('Hello from child!',name)


father1 = Father()
father2 = Father()

print(father1.age)
Father.age = 20
print(father2.age)