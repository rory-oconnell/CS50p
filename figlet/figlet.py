import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# fonts len == 425
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
        prompt = input("Input: ")
        f = Figlet(font=sys.argv[2])
        print(f.renderText(prompt))
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    randIndex = random.randint(0, len(fonts))
    randFont = fonts[randIndex]
    f = Figlet(font=randFont)
    prompt = input("Input: ")
    print(f.renderText(prompt))

else:
    sys.exit("Invalid usage")