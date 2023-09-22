# def main():
#     s= input("Please enter the time: ")
#     h , m = s.split(":")
#     if int(h)==7 and 00 <= int(m) <= 59 or int (h)== 8 and int (m)== 00:
#         print ("breakfast time")
#     elif 12 <= int(h) <= 13 and 00 <= int(m) <= 59 :
#         print ("lunch time")
#     elif 18 <= int(h) <= 19 and 00 <= int(m) <= 59 :
#         print ("dinner time")
#     else:
#         return ("None")
#     if __name__ == "__main__":
#         main()

def convert ( time ):
    hour, minute, = map(int, time.split(':'))
    decimal_time = hour + minute / 60
    return (decimal_time)

def main ():
    s = input("Please enter the time: ")
    decimal_time = convert(s)
    if 7.0 <= decimal_time <= 8.0:
        print ("breakfast time")
    elif 12.0 <= decimal_time <= 13.0:
        print ("lunch time")
    elif 18.0 <= decimal_time <= 19.0:
        print ("dinner time")
    else:
        return ("")

if __name__ == "__main__" :
    main()