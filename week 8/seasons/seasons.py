from datetime import date
import sys
import inflect

# YYYY-MM-DD
def main():
    try:
        d = input("Enter the b-day: ")
        year, month, day = date_test(d)
        birth_date = date(year, month, day)
        today_date = date.today()
        # subtracts as n days and hour. to only access the day parameter: "subtract.days"
        subtract = today_date - birth_date
        # convert to min = n days * 24 h * 60 s
        subt_to_minut = subtract.days * 24 * 60
        # convert to sentence
        p = inflect.engine()
        words = p.number_to_words(subt_to_minut, andword="")
        print(f"{words.capitalize()} minutes")
    except (ValueError,TypeError):
        sys.exit("FFFFFFFFFFFFFFFFFFFF")

def date_test(d):

    date_split = d.split("-")
    if len(date_split[0]) == 4 and len(date_split[1]) == 2 and len(date_split[2]) == 2 and 1 <= int(date_split[1]) <= 12:
        year, month, day = int(date_split[0]),int(date_split[1]),int(date_split[2])
        return year, month, day

if __name__ == "__main__":
    main()