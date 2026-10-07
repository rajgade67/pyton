n = 10 
a = -1
b= 1
for val in range(1 , n+1):
    c = a+b
    if(c % 2 != 0):
     print(c)
    a = b
    b = c