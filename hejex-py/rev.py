'''n = 321
rev = 0

while(n > 0):
    digit = n % 10 #321 % 10 = 1
    rev = rev * 10 + digit#0*10 + 1 =1
    n = n // 10 #321

print(rev)'''
    
num = 121
total = 0

for digit in str(num):
    total += int(digit)

print(total)
    

    
    

