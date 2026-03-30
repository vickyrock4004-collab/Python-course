#Dictionary 

map = {1: 'one', 2:'two'}

print(map)
print(type(map))

print(map[2])
print(map[1])

#accessing-map[1]
print(map.get(1))

#length
print(len(map))

#keys
print(map.keys())
print(map.values())

#items give output in list
print(map.items())

#insert
map[4] = 'four'
print(map)

#remove
map.pop(4)
print(map)

#clear
map.clear()
print(map)

#dict()
map = dict()

#task

map1 = {5: {'P': {5: "P"}, 6: "Q"}, 
        7: "R", 
        'Q': "S", 
        "S":'T'}

print(map1[map1[map1[5] [6]]])