import sys

if (len(sys.argv) == 2) and ((sys.argv[1]).endswith(".py")):
    """
    in this block i tried to check if the line is empty or is a comment, and if it was, it won't count
    that line and enters the "else-block" and ...
    """
    try:
        with open(sys.argv[1] , "r") as file:
            num_lines = 0
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                else:
                    num_lines += 1
        print(num_lines)
    except FileNotFoundError:
        sys.exit("File does not exist")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")
