import os
import sys
from pyfiglet import Figlet
import random
figlet = Figlet()


if len(sys.argv) == 1:
    choice = True
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        choice = False
else:
    sys.exit("Invalid usage")



figlet.getFonts()

if choice == False:
    try:
        figlet.setFont(font = sys.argv[2])

    except:
        sys.exit("Invalid usage")
else:
    font = random.choice(figlet.getFonts())

string = input("Input: ")

print("Output: ")
print(f"{figlet.renderText(string)}")





















