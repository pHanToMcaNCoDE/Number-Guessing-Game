import random

# Welcome Messages
print('Welcome To Num-Guess Palooza!')

print('Here\'re the rules:\n\n\t1. Guess any number between 1 and 100\n'
      '2. Keep guessing until you win!')

# The game selects any random number between a range
gameSelectedNumber = random.randint(1, 100)

# User selects the difficult level of the game
attempts = int(input('Select a difficulty level:\n1. Easy (8 chances)\n2. Medium (4 chances)\n' 
                     '3. Hard (2 chances): \n'))


# No. of Attempts for the game
count = 0


while True:
    try:
        # The user selects a number
        userSelection = int(input('Select any number between 1 and 100: '))

        # 4. If the number selected by the game is the same as the number the user selected,
        # then the user wins the game
        if userSelection == gameSelectedNumber:
            print('YOU WIN MATE!!! 😁 It took you ' + str(count) + ' attempts')
            break
        # If the number selected by the user is lesser than the number the game selected,
        # then the computer will prompt the user 'You selected way too low.'
        if userSelection < gameSelectedNumber:
            print('Select again. You selection is way too low 😭')
        else:
            # If the number selected by the user is greater than the number the game selected,
            # then the computer will prompt the user 'You selected way to high.'
            print('Select again. You selection is way too high 😒')
        count += 1
        # Confirm if the difficult limit has reached to end the game
        if attempts == count:
            try:
                print('Game Over, You\'ve reached your limit! It took you ' +
                      str(count) + ' attempts')
                break
            except ValueError:
                print('This is not a number! 😩')
    except ValueError:
        print('This is not a number! 😩')
