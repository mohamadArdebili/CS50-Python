# from random import randint
import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        first_num = generate_integer(level)
        second_num = generate_integer(level)
        answer = first_num + second_num
        tries = 0

        for i in range(4):
            if i < 3:
                print(f"{first_num} + {second_num} = ", end = "")
                try:
                    tries = int(input())
                except ValueError:
                    print("EEE")
                    continue
                if tries == answer:
                    score = score + 1
                    break
                else:
                    print("EEE")
            elif i == 3:
                print(f"{first_num} + {second_num} = {answer}")
                # exit the loop and print the score.
                break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        # again go to the loop
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()