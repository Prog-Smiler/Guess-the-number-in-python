import random

random_number = random.randint(1, 100)
print(random_number)

running = True
while running:
    

    user_guess = int(input("Enter the number: "))

    if user_guess < random_number:
        print("low")

    elif user_guess > random_number:
        print("high")

    elif user_guess == random_number:
        print("Correct")
        running = False