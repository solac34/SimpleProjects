import random


def main_game():
    word = list(str(input('Word to guess(type random to let system decide):')).lower())
    if word == 'random':
        word = random.choice(
            ['kaggle', 'hangman', 'science', 'preferences', 'bottle', 'cat', 'music', 'notebook', 'headphones',
             'game', 'movie', 'last', 'tea', 'coffee', 'furious', 'ford mustang', 'train', 'bus', 'paper', 'door'])
    current_q = 0
    failed_tries = 0
    guess_list = []
    true_guess_list = []
    while failed_tries < 9:
        if ''.join(guess_list) == ''.join(word):
            print(f"Successfully found the word:{guess.upper()}")
            new_game()
        current_q += 1
        guess = str(input(f'Guess - {current_q}:')).lower()  # take a guess from user
        if len(guess) > 1:
            if str(input("Are you sure you want to guess? In fail, you'll get a draw!(input y) for yes")) == 'y':
                if guess == ''.join(word):  # if user tried to guess the word
                    print(f"Successfully found the word:{guess.upper()}")
                    new_game()
                failed_tries += 1
            else:
                continue
        else:
            if guess in guess_list:
                print('this guess already been tried.')
                continue
            guess_list.append(guess)
            if guess in word:
                true_guess_list.append(guess)
            else:
                failed_tries += 1

            # print the current progress
            print("Current Progress", sep=': ')
            for ltr in word:
                if ltr == ' ':
                    print(end=' ')
                    continue
                if ltr in true_guess_list:
                    print(ltr, end='')
                else:
                    print("_", end='')
            print('\n')


def new_game():
    c = str(input('Would you like to play another game(input y to play a new game):'))
    if c.lower() == 'y':
        main_game()
    print('See you soon,sir!')
    exit(0)


main_game()
