def main():
    y = y_int("What's y? ")
    x = x_int("What's x? ")
    print(f"y is {y}")
    print(f"x is {x}")


def y_int(put_y):
    while True:
        try:
            return int(input(put_y))
        except ValueError:
            print("y is not an integer")



def x_int(put_x):
    while True:
        try:
            x = int(input(put_x))
        except ValueError:
            pass
        else:
            return x


main()