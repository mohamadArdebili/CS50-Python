import sys
from PIL import Image , ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

exten1 = (sys.argv[1]).split(".")
# [sys.argv[1], 'extensipn']

exten2 = (sys.argv[2]).split(".")
# [sys.argv[2], 'extensipn']

if len(sys.argv) ==3 and  (".png" or ".jpg" in sys.argv[1]) and ("png" or "jpg" in sys.argv[2]) and exten1[1] == exten2[1]:
    try:
        shirt = Image.open("shirt.png")
        img = Image.open(sys.argv[1])
        size = shirt.size
        img = ImageOps.fit(img, size)
        img.paste(shirt, shirt)
        img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

elif exten1[1] != exten2[1]:
    sys.exit("Input and output have different extensions")
