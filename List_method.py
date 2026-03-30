#list

'''
lis1 = [1, 2, 3]
lis2 = [4, 5, 6]
lis3 = lis1 + lis2

print(lis3)
'''
#length of list
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = lst1 + lst2

"""print(len(lst3))"""
#append add the one value to list last
lst1.append(4)
print(lst1)

#extend add the multiple value to list last
lst1.extend(lst2)
print(lst1)

#insert add the one value to index method to list

lst1.insert(0, 0)
print(lst1)

#count the value in list

print(lst1.count(4))

#find index value

print(lst1.index(3))

#Min and Max
print(min(lst1))
print(max(lst1))

#sort

lst2.extend(lst1)
print('Before sorting:', lst2)
lst2.sort(reverse=True)
print('After sorting:', lst2)

#SUM
print(sum(lst1))



#clear the list

'''lst1.clear()
print(lst1)'''

#mutablility

lst1[3] = 10000
print(lst1)

#pop empty to give the pop it remove the last value of list and other method using index to remove
"""lst1.pop()
print(lst1)"""

#remove
lst1.remove(10000)
print(lst1)




