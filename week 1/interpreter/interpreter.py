s = input("Enter the arg: ")
x , y , z = s.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))