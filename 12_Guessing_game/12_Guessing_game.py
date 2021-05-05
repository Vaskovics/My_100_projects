import random

EASY_LEVEL = 10
HARD_LEVEL = 5

number = random.randint(1, 100)


def play_game():
    print("I am thinking a number between 1 and 100")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guesses = 0
    if level == 'easy':
        guesses = EASY_LEVEL
    else:
        guesses = HARD_LEVEL

    while guesses > 0:
        print(f'You have left {guesses} attempts')
        guess = int(input("Please guess the number: "))
        if guess > number and guesses > 1:
            print("Sorry, you missed, pleas guess lower")
        elif guess < number and guesses > 1:
            print("Sorry, you missed, please guess higher")
        elif guess == number:
            print('You got it, well done!')
            break
        else:
            print(f"Game is over, you lose! Correct answer is {number}")
        guesses -= 1
        print("-" * 40)


while input('Do you want to play guessing game? Type "y" for yes and "n" for no: ') == 'y':
    play_game()