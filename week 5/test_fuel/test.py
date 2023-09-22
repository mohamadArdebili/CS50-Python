def main():
    n = (input("Enter the x/y: "))
    percentage = convert(n)
    print(gauge(percentage))

def convert(fraction):
    while True:
        x , y = fraction.split("/")
        try:
            x = int(x)
            y = int(y)
            if x > y:
                # again gets input from user.
                fraction = input("Enter the x/y: ")
                continue
            else:
                r_int = round((x*100)/y)
                return r_int
        except(ValueError, ZeroDivisionError):
            break

def gauge(percentage):
    if percentage >= 99:
         return "F"
    elif percentage <= 1:
         return "E"
    else:
         return str(percentage) +"%"

if __name__=="__main__":
    main()