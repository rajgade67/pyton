### WAPTO CHECK THE NUMBER IS PALLINDROME OR NOT #####
####RETURN TRUE IF PALLINDROME AND RETURN FALSE IF NOT PALLINDROME########


def chkPallindrome(num):
    temp = num 
    rev = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
    if(num == rev):
        return True
    else:
        return False
    
n = int(input("enter the number::"))   
print(chkPallindrome(n)) 