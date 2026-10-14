####@ 1. TO NEGLACT POSITIONAL PARAMETER #####
##### 2. assign value to parameter in function call
####  3. parameter name in functionb defination 
###and function call should be same 
####   4. flow should be right to left 







def emp(id, name ,sal, dept):
    print('ID:' , id)
    print('NAME:',name)
    print('SALARY:',sal)
    print('DEPT',dept)
    
emp(name ='ABC',sal= 10000,dept='IT',id =101)
print("################################")
emp(102,'ABCD',dept ='IT',sal= 1000000)