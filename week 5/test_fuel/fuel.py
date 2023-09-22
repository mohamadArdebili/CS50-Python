def main():
    while True:
        try:
            fraction = (input("Enter the x/y: "))
            percentage = convert(fraction)
            break
        except:
            pass
    print(gauge(percentage))

def convert(fraction):
    x , y = fraction.split("/")
    x = int(x)
    y = int(y)

    if x > y:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        r_int = round((x*100)/y)
        return r_int

def gauge(percentage):
    if percentage >= 99:
         return "F"
    elif percentage <= 1:
         return "E"
    else:
         return str(percentage) +"%"

if __name__=="__main__":
    main()