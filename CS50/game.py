import random
num = int(input('Level: '))
random_num = random.randint(1,num)
while True:
    try:
        guess_choice = int(input('Guess: '))
        if guess_choice > num:
            guess_choice == False
        elif guess_choice > random_num:
            print('Too large!')
            pass
        elif guess_choice < random_num:
            print('Too small!')
            pass
        else:
            print('Just right!')
            break
    except:
        pass