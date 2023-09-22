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


d = input("Enter the year: ")

if "/" in d:
    month, day, year = d.split("/")
    month = int (month)
    day = int (day)
    year = int (year)

    print (f"{year}-{month:02}-{day:02}")

elif " " in d:
    date = d.split(" ")
    print(date[2])