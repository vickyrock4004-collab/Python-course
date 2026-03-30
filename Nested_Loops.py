"""n = int(input('Enter n:'))

for i in range(1, n+1):
  for j in range (1, i+1):
    print(j, end=" ")
  print()"""


n = 4

'''for i in range(1, n+1):
    # spaces
    for j in range(n - i):
        print(" ", end="")

    # stars
    for j in range(2*i - 1):
        print("*", end="")

    print()'''



user = int(input('Enter your number:'))

'''for i in range(1, user+1):
  for j in range(1, i + 1):#1
    print('*', end="")#*
  print()'''

for i in range(3, user - 1):
  for j in range(1, i + 1):
    print('*', end="")
  print()