import random
while True:
    try:
        num = int(input('Level: '))
        random_num = random.randint(1,num)
        guess_choice = int(input('Guess: '))
        if num < guess_choice:
            pass
        elif guess_choice > random_num:
            print('Too large!')
            break
        elif guess_choice < random_num:
            print('Too small!')
            break
        else:
            print('Just right!')
            break  
    except:
        pass