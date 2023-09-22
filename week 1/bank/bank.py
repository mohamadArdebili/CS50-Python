s = input("Please say a welcome sentence: ").lower().strip()

if "hello" in s :
    print("$0")
elif (s[0]==("h")) and (s != ("hello")):
    print("$20")
else:
    print("$100")