while True:
    try:
        n = (input("Enter the x/y: "))
        x , y = n.split("/")
        x = int(x)
        y = int(y)
        r_int = round((x*100)/y)
        if 1 < r_int < 99:
            print (f"{r_int}%")
        elif 0 <= r_int <= 1:
            print("E")
        elif r_int > 100:
            raise ValueError
        elif r_int >= 99 :
            print("F")

    except (ValueError, ZeroDivisionError):
        print("x and y are not in correct format!!\nplz try an integer...")
    else:
        break
