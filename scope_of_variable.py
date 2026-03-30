a = 5
b = 12


def add():
  global a
  a = a+5
  print(a+b)

add()

print(a,b)

nums = [10,20,30,40,50,60]

res = nums[1:5:2]

print(res)

x = 10

def change_x():
  x = 20

change_x()

print(x)#10