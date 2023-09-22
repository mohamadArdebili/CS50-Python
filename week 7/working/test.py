import re
import sys
# 9:00 AM to 5:00 PM ->  09:00 to 17:00
# 9 AM to 5 PM
# 09:00 AM - 17:00 PM
# 9:60 AM to 5:60 PM
def main():
    print(convert(input("Hours: ")))

def convert(s):
    start_time , end_time = s.split(" to ")
    if ":" in start_time and ":" in end_time:
        h1, m1, am_pm1 = re.findall('\d+|\w+', start_time)
        h2, m2, am_pm2 = re.findall('\d+|\w+', end_time)
        h1 = int(h1)
        h2 = int(h2)
        m1 = int(m1)
        m2 = int(m2)
        # ValueErrors
        if m1 >= 60:
            raise ValueError
        if m2 >= 60:
            raise ValueError
        if "PM" in am_pm1 and h1 != 12 and 0<= m1 <=59:
            h1 += 12
        elif "AM" in am_pm1 and h1 == 12:
            h1 = 0
        if "PM" in am_pm2 and h2 != 12 and 0<= m2 <=59:
            h2 += 12
        elif "PM" in am_pm2 and h2 == 12:
            h2 = h2
        elif "AM" in am_pm2 and h2 != 12:
            h2 = h2
        elif "AM" in am_pm2 and h2 == 12:
            h2 = 0
        else:
            raise ValueError
        return f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}"

    elif ":" not in start_time and ":" not in end_time and " " in start_time and " " in end_time:
        h1, am_pm1 = re.findall('\d+|\w+', start_time)
        h2, am_pm2 = re.findall('\d+|\w+', end_time)
        h1 = int(h1)
        h2 = int(h2)
        if "PM" in am_pm1 and h1 != 12:
            h1 += 12
        elif "AM" in am_pm1 and h1 == 12:
            h1 = 0
        if "PM" in am_pm2 and h2 != 12:
            h2 += 12
        elif "PM" in am_pm2 and h2 == 12:
            h2 = h2
        elif "AM" in am_pm2 and h2 != 12:
            h2 = h2
        elif "AM" in am_pm2 and h2 == 12:
            h2 = 0
        else:
            raise ValueError
        return f"{h1:02d}:00 to {h2:02d}:00"
    else:
        raise ValueError

if __name__ == "__main__":
    main()