#Inheritance lets one class reuse properties and methods of another class instead of rewriting everything.


"""class Vehicle:#parent class
  no_of_wheels = 4

  def moveForward(self):
    print('Vehicle is moving forward!')

#single inheritance
class Car(Vehicle):#child class / sub class
  no_of_airbags = 3

#Hierachical inheritance
class Bike(Vehicle):
  mileage = 60.0

#Multi-level inheritance
class Maruthi(Car):
  mileage = 25.0


car1 = Maruthi()
print(car1.no_of_airbags)
print(car1.no_of_wheels)
print(car1.mileage)
car1.moveForward()"""

#Multiple inheritance

'''class Father:
  hair_color = 'White'

class Mother:
  hair_color = 'black'
  eye_color = 'blue'

class Child(Father,Mother):
  no_of_leg = 2

Child1 = Child()
print(Child1.no_of_leg)
print(Child1.hair_color)
print(Child1.eye_color)'''



class Vehicle:#parent class
  no_of_wheels = 4

  def moveForward(self):
    print('Vehicle is moving forward!')


class Car(Vehicle):#child class / sub class
  no_of_airbags = 3


class Bike(Vehicle):
  mileage = 60.0


class Maruthi(Car):
  mileage = 25.0

class Toyota(Car):
  mileage = 30.0


class Toythi(Maruthi, Toyota):
  has_touchscreen = True



car1 = Toythi()
print(car1.no_of_airbags)
print(car1.no_of_wheels)
print(car1.mileage)
car1.moveForward()

#task

class Father:
  hair_color = 'White'

  def music(self):
    print("Kuthu paatu!")

class Mother:
  hair_color = 'black'
  eye_color = 'blue'

  def music(self):
    print('Melody paatu')

class Child(Father,Mother):
  no_of_leg = 2

Child1 = Child()
Child1.music()