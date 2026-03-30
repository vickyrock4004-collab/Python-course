class Car:
  no_of_wheels = 0
  mileage = 0.0
  no_of_airbags = 0

  def moveForward(self):
    print('Car is moving!')

  def moveBackward(self):
    print('Car is moving backward!')

car1 = Car() #instance of a class - object: Instantiation
print(car1.no_of_wheels)
car1.mileage = 25.0
print(car1.mileage)


class Bank_Account:
  customer_name = ""
  balance = 0.0
  account_number = 0


customer1 = Bank_Account()
customer1.customer_name = "Vignesh"
customer1.balance = 26.0
customer1.account_number = 234569706

print(customer1.customer_name)
print(customer1.balance)
print(customer1.account_number)