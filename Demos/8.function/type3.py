#####WITHOUT PASSING PARAMETER ############
###### WITH RETURNING VALUE  #########

def addition():
    num1 = int(input('enter the number'))
    num2 = int(input('enter the number'))
    
    add = num1 + num2
    
    return add
res = addition()
print(res)