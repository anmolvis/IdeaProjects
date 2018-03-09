import random
high = 10
number = random.randint(1, high)
print("You have five chances to guess\nYou can Enter 0 if u don't want to play\n")
num = int(input("Enter the number: "))
while num != 0:
    if num == number:
        print("Number guessed is correct\n")
        break
    elif num > number:
        print("Choose smaller number\n")
    else:
        print("Choose greater number\n")
    num = int(input("Enter the number: "))
print("Thanks for playing\n")
