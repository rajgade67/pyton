##### recursive is alternativwe of while loop  ####

def series(n):  
    if(n > 0):
        print(n)
        series(n - 1)

num = int(input("enter the number"))
series(num)