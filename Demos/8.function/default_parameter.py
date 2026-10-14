##### 1.TO MAKE PARAMETER OPTIONAL
####  2. PARAMETER - DEFAULT (ASSINIMGG VALUE TO PARAMETER IN FUNCTION DEFINATION)
####  3. IF WE PASS VALUE TO DEFAULT PARAMETER, IT TAKES PASSED VALUE 
       ##IF WE DONT PASS VALUE TO DEFAULT VALUE PARAMETER ,IT TAKES DEFAULT VALUE
#### 4. FLOW FROM RIGHT TO LEFT

def emp(id,name,salary = 0,dept = 'Backoffice'):  ###dept = 'backoffice' kela ani salary 0 keli
    print('ID:' ,id)
    print('NAME:',name)
    print('SALARY:',salary)
    print('DEPT:',dept)

emp(101,'ABC',10000,'IT')   
print('###############################')

emp(102,'BC',5000)

print('###############################')
emp(103,'RAM')