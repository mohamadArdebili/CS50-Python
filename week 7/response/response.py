import validators

s = input("Please enter the email-address to start validation:\n")
validation = validators.email(s)
if validation == True :
    print("Valid")
else:
    print("Invalid")
