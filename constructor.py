
#when create the objecct automatical call itself this the constructor


class Car:
  def __init__(self):
    print("This is constructor")
    self.no_of_wheels = 0
    self.mileage = 0.0
    self.no_of_airbags = 0



  

  def moveForward(self):
    print('Car is moving!')

  def moveBackward(self):
    print('Car is moving backward!')


car1 = Car() #instance of a class - object: Instantiation
print(car1.mileage)

car2 = Car()
print("Mileage:", car2.mileage)
car2.mileage = 25.0
print("Mileage:", car2.mileage)

car3 = Car()
car3.moveForward()
