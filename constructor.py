
#when create the objecct automatical call itself this the constructor


'''class Car:
  def __init__(self, carname, no_of_wheels, no_of_airbags):
    print("This is constructor")
    self.no_of_wheels = no_of_wheels
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



car1 = Car() #instance of a class - object: Instantiation
print(car1.mileage)

car2 = Car()
print("Mileage:", car2.mileage)
car2.mileage = 25.0
print("Mileage:", car2.mileage)

car3 = Car('BMW', 4,6)
print(car3)
print(car3.no_of_airbags, car3.carname, car3.no_of_wheels)
car3.moveForward()'''

#task
class Bank_Account:
  def __init__(self, customer_name, balance, account_number):
    self.customer_name = customer_name
    self.balance = balance
    self.account_number = account_number

  def __str__(self):
    return self.customer_name

customer1 = Bank_Account('Vignesh', 2040689, 1234)

print(customer1.account_number,customer1.balance, customer1.customer_name)
print(customer1)