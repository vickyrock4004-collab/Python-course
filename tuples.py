#tuples not update the element but we can recreate the variable



tup = (170, 180, 100, 999)

print(tup[0])



#lenght

print(len(tup))

#min and max
print(min(tup), max(tup))

#count method is using for count the value how many time repeat in variable
print(tup.count(100))

#index
print(tup.index(180))


#conventing the list to tuple and tuple to list

lst = list(tup)
print(type(lst))

tup1 = tuple(lst)
print(type(tup1))

#task

fruits = ('apple', 'banana', 'mango', 'kiwi', 'strawberry')
print(fruits)

fruits += ('grapefruits',)
print(fruits)
