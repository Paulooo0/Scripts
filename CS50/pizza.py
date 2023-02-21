import sys
import csv
from tabulate import tabulate

def main():
    check_command_line()
    
    try:
        file = open(sys.argv[1].rstrip(), 'r')
        reader = csv.reader(file)
    except FileNotFoundError:
        sys.exit('File does not exist')
    
    data = []
    for row in reader:
        data.append(row)
    print(tabulate(data[1:], headers=data[0], tablefmt="grid"))


def check_command_line():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif not '.csv' in sys.argv[1]:
        sys.exit('Not a CSV file')


if __name__ == '__main__':
    main()