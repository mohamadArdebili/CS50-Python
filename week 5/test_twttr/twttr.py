def main():
    s = input("Enter the string: ")
    shortened = shorten(s)
    print(shortened)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u" , "A", "E", "I", "O", "U"]
    new_string = ""
    for c in range(len(word)):
        if word[c] not in vowels:
            new_string += word[c]
    return new_string
if __name__=="__main__":
    main()