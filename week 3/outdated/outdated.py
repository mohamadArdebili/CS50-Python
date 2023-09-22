# M / D / Y convert to   Y-M-D
months= [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]

while True:
    d = input("Enter the year: ").strip()

    if "/" in d:
        month, day, year = d.split("/")
        if month.isdigit() and day.isdigit() and year.isdigit() :
            month = int (month)
            day = int (day)
            year = int (year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print (f"{year}-{month:02}-{day:02}")
                break
    elif " " in d and "," in d:
        date = d.split(" ")
        if date[0].isalpha():
            year = date[2]
            month = date[0].title()
            day = int(date[1].replace("," , ""))
            if month in months:
                m = int(months.index(month)+1)
                if 1 <= m <= 12 and 1 <= day <= 31:
                    print(f"{year}-{m:02}-{day:02}")
                    break

