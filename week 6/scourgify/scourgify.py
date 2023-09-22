import csv
import sys

output = []
if len(sys.argv) ==3:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name , first_name = (row["name"]).split(", ")
                house = row["house"]
                output.append({"first": first_name , "last": last_name , "house": house})

                with open(sys.argv[2],"w") as file_2:
                    writer = csv.DictWriter(file_2 , fieldnames = ["first","last","house"])
                    writer.writeheader()
                    for row in output:
                        writer.writerow({"first": row["first"],"last": row["last"],"house": row["house"]})

                    #writer.writerow({"first": first_name , "last": last_name , "house": house })
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")