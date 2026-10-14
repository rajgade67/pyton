#### WITH PASIING PARAMETER/ ARGUMENTS   #######
#### WITH RETURNING VALUE #############

def addition(num1, num2):
    
    add = num1 + num2

    return add  

num1 = int(input('enter the number 1:'))
num2 = int(input('enter the number 2:'))

res = addition(num1,num2)
print('addition' ,res)