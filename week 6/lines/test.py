import sys





#1
"""
if (len(sys.argv) == 2) and ((sys.argv[1]).endswith(".py")):
    # removing the ".py" from command-line argument.
    file_name = (sys.argv[1]).strip(".py")
    with open(sys.argv[1] , "r") as file:
        x = len(file.readlines())
        print('Total lines:', x)

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")
""""
#2
"""
if (len(sys.argv) == 2) and ((sys.argv[1]).endswith(".py")):
    with open(sys.argv[1] , "r") as file:
        lines = 0
        for line in file:
            if line.strip() or "#" not in line:
                lines += 1
    print(lines)


elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")
"""
#3
"""

if (len(sys.argv) == 2) and ((sys.argv[1]).endswith(".py")):
    with open(sys.argv[1] , "r") as file:
        num_lines = 0
        for line in file:
            line = line.strip()
            if line == "" or line.startswith("#") or (line.startswith('"""') and line.endswith('"""')):
                continue
            else:
                num_lines += 1
    print(num_lines)


elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

"""