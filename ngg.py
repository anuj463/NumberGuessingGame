import random as rnd

a = rnd.randint(1,100)

num = int(input("Enter the number between 1 and 100:"))

while num != a:
    if num <1 or num >100:
        print("Invalid number")
        break
    elif num < a :
        print("Too low!!")
        break
    elif num > a:
        print("Too high!!")
        break
    else:
        print("Invalid input!")
        num = int(input("Enter the number between 1 and 100:"))
    
    
    
    
    if num == a:
        print("You guesses it right!!")
        
