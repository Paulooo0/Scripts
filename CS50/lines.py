import sys
def main():
    check_argument()

    try:
        file = open(sys.argv[1], 'r')
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit('File does not exist')

    count = 0
    for line in lines:
        if check_content(line) == False:
            count += 1
    print(count)


def check_argument():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif not '.py' in sys.argv[1]:
        sys.exit('Not a Python file')


def check_content(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False


if __name__ in '__main__':
    main()