def main():
    Input = (input('Input: '))
    print('Output:\n',figlet.renderText(Input))
    
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()

try:
    if len(sys.argv) < 2:
        figlet.setFont(font=random.choice(figlet.getFonts()))
    else:
        pass
except:
    print('error 1')
    
if '-f' in sys.argv or '--font' in sys.argv:
    figlet.setFont(font=sys.argv[2])
else:
    pass
    
if __name__ == '__main__':
    main()