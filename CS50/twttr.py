def main():
    put=shorten(input('Input: '))
    print('Output:',put)


def shorten(text):
    for char in 'aeiouAEIOU':
        text = text.replace(char,'')
    return text

if __name__ == "__main__":
    main()