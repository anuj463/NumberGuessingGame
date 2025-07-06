# Python project to implement number guessing game
# Author: Anuj Savant
# Date: 6/7/25


import random as rnd

a = rnd.randint(1,100)

num = int(input("Enter the number between 1 and 100:"))

while num != a:
    if num <1 or num >100:
        print("Invalid number")
        break

    elif num < a :
        print("Too low!!")
        num = int(input("Enter the number between 1 and 100:"))

    elif num > a:
        print("Too high!!")
        num = int(input("Enter the number between 1 and 100:"))
    
    elif num == a:
        print("You guessed right!!")
        break
