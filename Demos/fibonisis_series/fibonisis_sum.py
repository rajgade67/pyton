n  = 10
a = -1 
b = 1
sum = 0
for val in range( 1 , n+ 1):
    c = a + b  
    sum = sum + c
  
    a = b
    b =c
print(sum)