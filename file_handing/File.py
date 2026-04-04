#file.read()

'''file = open('text/info.txt', 'r')
print(file.read())

#seek using to move the cursor backward
print(file.read)
file.seek(0)
#tell is cursor is where locate
print(file.tell())
print(file.read())'''


#file.readline()
'''print(file.readline())

#file.readlines
print(file.readlines())
file.close()'''

#write is delete the entire previous text and write new text
'''file = open('text/info.txt', 'w')

file.write('Hello this is vignesh')


file.close()'''

#append just add the text
'''file = open('text/info.txt', 'a')

file.write('Hello this is vignesh')
lst = ['Hi hihi']
file.writelines(lst)


file.close()'''

#with open

with open('text/info.txt','r') as file:
  print(file.read())

#flush is 