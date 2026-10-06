gender = input('enter the gender:')
age = int (input('enter the age'))

if(gender == 'f'):
    if(age >= 18):
        print("girl is eligible")
    else:
        print("pahai kar le")
else:
    if(age >= 21):
        print('boy is eligible')
    else:
        print('pahle kama lo')