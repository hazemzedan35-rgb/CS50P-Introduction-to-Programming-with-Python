import pyfiglet

import sys 

import random
# get the whole fonts in pyfiglet lebrary
font = pyfiglet.Figlet().getFonts()

# If no command line arguments, choose randomly a font
if len(sys.argv) ==1:
    random_font = random.choice(font)
    f = pyfiglet.Figlet(font=random_font)
    print(f.renderText(input("Input: ")))

# If two command-line arguments, one to set the font, and other a valid font, set the font
elif len(sys.argv) ==3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in font:
    f = pyfiglet.Figlet(font=sys.argv[2])
    print(f.renderText(input("Input: ")))

# If the user input wrong font or forget -f or -n the program will stop 
else:
    sys.exit("Invalid usage")




