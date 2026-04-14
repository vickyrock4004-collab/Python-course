#List Comprehension

arr = [1,2,3,4,5,6]
odd = []

'''for i in arr:
  if(i % 2 == 1):
    odd.append(i)
print(odd)'''

odd = [i for i in arr if(i % 2 == 1)]
print(odd)

even = [i for i in arr if(i % 2 == 0)]
print(even)

'''lst = []
for i in range(1,101):
  lst.append(i)
print(lst)'''
  
lst = [i for i in range(1, 101)]
print(lst)

