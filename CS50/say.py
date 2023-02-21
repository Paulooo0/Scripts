import cowsay
import sys

while True:
    try:
        if len(sys.argv) == 2:
            cowsay.trex('cade o ' + sys.argv[1])
            break
    except (ValueError, NameError):
        print()
        pass
    
from sayings import goodbye
if len(sys.argv) == 2:
    goodbye(sys.argv[1])