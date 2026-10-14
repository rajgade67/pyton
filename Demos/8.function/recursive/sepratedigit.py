#### Separate Digits Using Recursive Function ###

def separate(num):
    if num == 0:
        return

    separate(num // 10)
    print(num % 10)

n = int(input("Enter the number: "))
separate(n)