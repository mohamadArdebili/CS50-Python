from pyfiglet import Figlet
import sys
figlet = Figlet()

fonts = figlet.getFonts()
font_format = ""

if len(sys.argv) == 3 and sys.argv[2] in fonts and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    font_format = figlet.setFont(font=sys.argv[2])
    s = input("Input: ").strip()
    print(figlet.renderText(s))

else:
    sys.exit("Invalid usage")
