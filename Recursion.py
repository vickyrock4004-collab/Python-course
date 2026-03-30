#Recursion = a function calling itself to solve a problem.

def add(n):
  print(n)
  return add(n-1)



#base case (STOP condition) “Stop here”
#resursive case (WORK + repeat) “Keep going”


def sum_of_n(n):
  #Base Case
  if(n == 1):
    return 1

  #Resursive Case
  return n + sum_of_n(n-1)


print(sum_of_n(5))

'''
5 + (5-1)=4
5+4(4-1)=3
5+4+3(3-1)=2
5+4+3+2(2-1)=1
5+4+3+2+1=15
'''

#task

def factorcial(n):
  if(n == 0):
    return 1
  
  else:
    return n * factorcial(n-1)
  
result = factorcial(5)

print(result)

