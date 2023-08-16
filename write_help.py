import os

from random import choice
from string import ascii_lowercase

FILENAME = 'sowpods.txt'
os.chdir(os.path.dirname(__file__))


def get_rand_word(filename):
    with open(filename, 'r') as f:
        return choice([x.strip() for x in f]).lower()


def print_game(wrong, word, letters):
    print('\nWrong guess:', ', '.join(wrong))
    for i in letters:
        if i is None:
            print(' ', end=' ')
        else:
            print(i, end=' ')
    print()
    for i in word:
        if i != ' ':
            print('-', end=' ')
        else:
            print(' ', end=' ')
    print()


def get_letter(attempt, guess):
    user_input = input(f'> Guess a letter ({attempt} attempts left): ').lower()
    if len(user_input) != 1 or user_input not in ascii_lowercase:
        print("> Please input a letter!")
    elif user_input in guess:
        print(f"> You have guessed '{user_input}' before")
    else:
        return user_input


def play(word):
    attempt = 6
    guess, guess_wrong = [], []
    letters = []
    for i in word:
        i = None if i != ' ' else i
        letters.append(i)
    while attempt > 0:
        print_game(guess_wrong, word, letters)
        if None not in letters:
            print('> You win!')
            break
        user_letter = get_letter(attempt, guess)
        if user_letter is not None:
            for i in range(len(word)):
                if user_letter == word[i]:
                    letters[i] = user_letter
            guess.append(user_letter)
            if user_letter not in letters:
                guess_wrong.append(user_letter)
                attempt -= 1
    else:
        print_game(guess_wrong, word, letters)
        print('> You lose...')
        print(f'> Answer: {word.capitalize()}')


if __name__ == "__main__":
    # word = get_rand_word(os.path.join('data', FILENAME))
    play('Hello world')



# Программа получает случайное слово (word) из текстового файла data/sowpods.txt

# Массив letters заполняется символами из слова word, где все символы, кроме пробела заменяются на None.

# Цикл выполняется пока число попыток больше 0.
# - Выводятся неверные символы, массив letters и символы строки word, причем все символы кроме пробела заменены дефисом.
# - Если в letters не осталось None, выводиться 'Вы выиграли', выход из цикла, заканчивается программа.
# - Запрос символа от пользователя, если введены более 1 символа или не ascii символ выводиться предупреждение, если такой символ вводил уже пользователь так же выводиться сообщение об этом.
# - Если в word есть введенный символы, то на соответствующие места в letters вносятся эти символы. и этот символ вноситься в массив введенных символов.
# - Если введенного символа нет в letters то этот сивмол вноситься в массив неправильных символов. Уменьшается количество попыток на 1. 
