import random

def main():
    level = get_level()
    score = main_game(level)
    print('Score:',score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                return level
        except:
            pass

def generate_integer(level):
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)
        return x,y

def check_result(x,y):
    chances = 3
    while chances != 0:
        try:
            result = int(input(f'{x} + {y} = '))
            if result == x+y:
                return True
            else:
                print('EEE')
                chances -= 1
        except ValueError:
            print('EEE')
            chances -= 1
    print(f'{x} + {y} = {x+y}')
    return False

def main_game(level):
    round = 0
    score = 0
    while round <10:
        x,y = generate_integer(level)
        answer = check_result(x,y)
        if answer == True:
            score += 1
        round += 1
    return score

if __name__ == "__main__":
    main()