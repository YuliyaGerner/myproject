import random, sys
from typing import List

WORD_LIST = [
"банан", "арбуз", "яблоко", "дыня", "виноград", "манго", "личи", "апельсин",
 "мандарин", "груша", "персик", "абрикос", "слива", "клубника", "малина"
           ]

GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST)
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
letter_storage = []


def print_word_to_guess(letters: List) -> None:

    print("Слов отгадать: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:

    print("Вы отгадали {0}/{1}.".format(current, total))




def beginning() -> None:

    print("Привет!\n")
    while True:
        name = input("Введите имя\n").strip()
        if name == '':
            print("Неа! Введите имя!")
        else:
            break


def ask_user_to_play() -> None:

    print("Давайте поиграем\n")
    while True:
        gameChoice = input("Да или нет\n").upper()
        if gameChoice == "ДА" or gameChoice == "Y":
            break
        elif gameChoice == "НЕТ" or gameChoice == "N":
            sys.exit("Ну и ладно. Подуууумаешь....")
        else:
            print("Введите Да или Нет")
            continue


def prepare_secret_word() -> None:

    for character in SECRET_WORD:
        GUESS_WORD.append("-")
    print("Ну давайте, отгадывайте", LENGTH_WORD, "букавок")
    print("Можно ввести только одну букавку от а-я\n\n")
    print_word_to_guess(GUESS_WORD)


def guessing() -> None:

    guess_taken = 1
    MAX_GUESS = 5
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Выберите букавку\n").lower()
        if not guess in ALPHABET:
            print("Выберите букавку от а-я")
        elif guess in letter_storage:
            print("Уже выбирали эту букву!")
        else:
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("Ай молодца! Отгадали!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if not '-' in GUESS_WORD:
                    print("Вы победили!")
                    print("Игра окончена!")
                    break
            else:
                print("А нету здесь такой букавки! Попробуйте еще!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 5:
                    print(" Пардон, но Вы проиграли! Вот же слово {0}".format(SECRET_WORD))


if __name__ == "__main__":
    beginning()
    ask_user_to_play()
    prepare_secret_word()
    guessing()