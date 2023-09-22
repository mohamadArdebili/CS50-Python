import random

while True:
    try:
        n = int(input("Level: "))
        if n >=0:
            num = random.randint(1,n)
            break
        else:
            False
    except ValueError:
        False

while True:
    try:
        user_guess = int(input("Guess: "))
        if user_guess < num:
            print("Too small!")
        elif user_guess > num:
            print("Too large!")
        elif user_guess == num:
            print("Just right!")
            break
    except ValueError:
        False