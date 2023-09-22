import csv
import sys
from tabulate import tabulate

data= []
if ".csv" in sys.argv[1]:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
elif ".csv" not in sys.argv[1]:
    sys.exit("File does not exist")
print(tabulate(data[1:], headers=data[0], tablefmt='grid'))