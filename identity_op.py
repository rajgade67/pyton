##########__________#identity operator__________@@@@@@@@@@@@@@@@@@@@@@@@@@



x = 10
#Immutable  - reuse ( we use and use with them)

y = 10
z = 20


li1 = [10 , 20] 
# Mutable - NEW MEMORY ALLOCATed (we can change them)


li2 = [10 , 20] 

print(id (x))
print(id (y))
print(x is y)
print(x is z)

print(id (li1))
print(id (li2))

 
 
