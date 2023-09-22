import random
import sys
import math

"""
Wanted the program to show introduction, just once in the beginning; not every time that condition line 19-53
was not met. So i put the introduction at line 101 and then, program begins from main().
"""

def main():

    # quantification of the lower and upper-bound.
    lower_bound = check_lower_int()
    upper_bound = check_upper_int()

    guess_limits = guess_limit(upper_bound,lower_bound)

    # check if the lower_bound < upper_bound:
    if lower_bound < upper_bound:

        rand_number = generate_integer(lower_bound, upper_bound)
        print(f"Great. Now go on...\nYou've got {guess_limits} chances.")
        guess_counter = 0

        while guess_counter < guess_limits:
            try:
                guess = int(input("Guess: "))
                # if 'guess' is in the range:
                if lower_bound <= guess <= upper_bound:
                    # checking for correct answer. then breaks the loop and goes to line 49.
                    if guess == rand_number:
                        break
                    if guess_counter < guess_limits:
                        guess_counter = guess_counter + 1
                        print(user_guess(guess, rand_number, guess_counter, guess_limits))
                    elif guess_counter == guess_limits:
                        raise ValueError
                # if 'guess' is not in the range:
                elif guess > upper_bound:
                    print(f"{guess} is bigger than the upper-bound!!!\nTry again...")
                elif guess < lower_bound:
                    print(f"{guess} is smaller than the lower-bound!!!\nTry again...")

            except ValueError:
                print ("Oh no! plz enter an integer...")
            except EOFError:
                sys.exit("\nHave a nice day🖐️")

        if guess == rand_number:
            print(f"Great!!! You've read my mind in {guess_counter + 1} steps.")

    # check if the lower_bound < upper_bound:
    else:
        print("Sorry, but the upper-bound must be greater then the lower-bound. Try again...")
        main()


    # asking the player to playing again or not
    print("Do you want to play again?", end = " ")
    playagain=input()
    while playagain=="yes" or playagain=="y" or playagain=="Yes":
        main()
    else:
        sys.exit("Bye🖐️")


def intro():
    print("\n\n\t-------- Welcome to Guessing Game --------\n")

# limitation of guesses depends on the 'upper_bound,lower_bound'.
def guess_limit(upper_bound,lower_bound):
    return round(math.log(upper_bound - lower_bound + 2, 2))

def check_lower_int():
    # checking the first number; if it's not an int, will ask to enter an int again
    while True:
        try:
            lower_bound = int(input("Enter the lower-bound of range: "))
        except ValueError:
            pass
        except EOFError:
            sys.exit("\nBye🖐️")
        else:
            return lower_bound
def check_upper_int():
    # checking the second number; if it's not an int, will ask to enter an int again
    while True:
        try:
            upper_bound = int(input("Enter the upper-bound of range: "))
        except ValueError:
            pass
        except EOFError:
            sys.exit("\nBye🖐️")
        else:
            return upper_bound

def generate_integer(lower_bound, upper_bound):
    # generates an int between lower & upper bound.
    return random.randint(lower_bound, upper_bound)

def user_guess(guess, rand_number, guess_counter, guess_limits):

    # checking if 'guess' is more or less than the 'rand_number'
    if guess_counter < guess_limits:
        if guess < rand_number:
            return ("It's too low! Try again...")
        elif guess > rand_number:
            return ("It's too much! Try again...")
    elif guess_counter == guess_limits:
        return f"Sorry, but the answer was: {rand_number}"

# introduction of the game
intro()
if __name__ == "__main__":
    main()