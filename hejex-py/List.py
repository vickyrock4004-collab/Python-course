#find index value

'''nums = [2,7,11,15]




for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if(nums[i] + nums[j] == 9):
            print([i,j])'''
        
'''nums = [3,2,4]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):#0
        if(nums[i] + nums[j] == 6):
            print([i,j])'''

'''nums = [3,3]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if(nums[i] + nums[j] == 6):
            print([i,j])'''





#remove same number

'''nums = [1, 2, 3, 2, 1]

newlst = []

for i in nums:
    if(i not in newlst):
        newlst.append(i)

print(newlst)'''


#convert


lst1 = [11,13,50]#111350

lst2 = ""

for i in lst1:
    lst2 += str(i)

print(lst2)
