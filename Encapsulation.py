#Binding of variables and methods


class Car:
  def __init__(self, carname, no_of_wheels, no_of_airbags):
    print("This is constructor")
    self.__no_of_wheels = no_of_wheels #private
    self.mileage = 0.0
    self.no_of_airbags = no_of_airbags
    self.carname = carname

  def __del__(self):
    print('This is a Destructor', self )


  def moveForward(self):
    print('Car is moving!')

  def moveBackward(self):
    print('Car is moving backward!')

  def __srt__(self):
    return (self.carname)
   

  #getter
  def get_no_of_wheels(self):
    return('No of wheels:', self.__no_of_wheels)
  
  #setter
  def set_no_of_wheels(self, no_of_wheels):
    self.__no_of_wheels = no_of_wheels



car3 = Car('BMW', 4,6)
print(car3)
print(car3.no_of_airbags, car3.carname, car3.get_no_of_wheels())
car3.moveForward()

#car3.__no_of_wheels = 7
#print(car3.__no_of_wheels)

car3.set_no_of_wheels(9)
print(car3.get_no_of_wheels())
