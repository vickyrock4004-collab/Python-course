"""set1= {1,2,3,4}
print(set1)
print(type(set1))

#add element we add the element in unorder
#True is 1 and False is 0 already 1 is assinged

set1.add(False)
print(set1)

#remove

set1.remove(0)
print(set1)

#clear

set1.clear()
print(set1)

#list convent to set
#constructor

lst = [65, 8, 7, 83]
set2 = set(lst)
print(set2)"""

set1 = {2,3,4}
set2 = {1,4,5}

#Union 
'''print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))

for i in set1:
  print(i)


print(1 in set2)'''

#task

set1 = {1,2,3,4}
set2 = {4,5}
set3 = {2,3,4,5,7,8}

print(set1.union(set2).intersection(set3))#{1,2,3,4,5} #{2,3,4,5}
