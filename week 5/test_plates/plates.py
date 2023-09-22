
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalpha():
        return True
    elif 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for c in s:
            if c.isdigit() :
                nums = s.find(c)
                if (s[nums:].isdigit() and int(c) != 0):
                    return True
                else:
                    return False
if __name__ == "__main__":
    main()