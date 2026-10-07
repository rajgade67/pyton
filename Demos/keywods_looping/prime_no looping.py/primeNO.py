num = 7
for i in range(2, num):
    if(num %i ==0):
        print(f"not prime")
        break
else:
     print(f"it is prime")