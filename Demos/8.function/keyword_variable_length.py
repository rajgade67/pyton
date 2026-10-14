### 1. to pass multiple values with meaning to function 
### 2. MENTION 2 ASTRICK SYMBOLS BEFIRE PARAMETR NAME IN FUNCTION
### 3. passeddata stored in dictonary format
### 4. use for loop on dict.items() to get values and keys

def emp(**data):
    for key,val in data .items():
        print(key, ':' ,val)
        
emp(id = 101,age = 35 ,add = 'pune',sal =5000,dept='Admin')