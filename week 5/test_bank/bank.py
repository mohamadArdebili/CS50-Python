def main():
    s = input("Please say a welcome sentence: ")
    amount = value(s)
    print("$" + amount)

def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return 0
    elif (greeting[0]==("h")) and (greeting != ("hello")):
        return 20
    else:
        return 100

if __name__=="__main__":
    main()