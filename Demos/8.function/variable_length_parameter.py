### 1. TO PASS MULTIPLE VALUE TO FUNCTION
### 2. MENTION 1 ASTRICK SYMBOL BEFORE PARAMETER NAME IN FUNCYION DEFINATION
### 3. PASSED VALUES ARE STORED IN TIPLE FORMAT
### 4. USE FOR LOOP TO ITERATE VALUES FROM TUPLE


def add(*data):
    sum = 0
    for val in data:
        sum += val 
    return sum

res =add(10,20 ,30,40)
print(res)