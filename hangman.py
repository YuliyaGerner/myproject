import json
import random
with open ('wordlist.json', 'r', encoding= 'utf-8') as f:
    text=json.load (f)


def play_game(words):
HANGMANPICS = ['''

    +-----+
    |     |
          |
          |
          |
          |
============''','''

    +-----+
    |     |
    o     |
          |
          |
          |
============''',''' 

    +------+
    |      |
    o      |
    |      |
           |
           |
=============''',''' 

    +------+
    |      |
    o      |
   /|      |
           |
           |
=============''',''' 

    +------+
    |      |
    o      |
   /|\     |
           |
           |
=============''',''' 
               
    +------+
    |      |
    o      |
   /|\     |
   /       |
           |
=============''','''
               
    +------+
    |      |
    o      |
   /|\     |
   / \     |
           |
=============''']


def getRandomWord (wordlist):

     wordIndex = random.randint (0, len (wordlist) -1)
     return wordList [wordIndex]

def displayBoard (HANGMANPICS, missedletters) correctLetters,secretWord):
     print (HANGMANPICS [len(missedLetters)])
     print ()

     print ('Неправильные буквы:', end= ' ')
     for letter in missedLetters:
         print (letter, end=' ')
     print()

     blanks = '*'*len(secretWord)
     for i in range (len (secretWord)):
         if secretWord [i] in correctLetters:
              blanks = blanks [:i] + secretWord [i] + blanks [i+1:]

     for letter in blanks:
         print(letter, end=' ')
     print()

def getGuess (alreadyGuessed) :

     while True:
     print ('Введите букву')
     guess = input()
     guess = guess.lower()
     if len(guess)  !=  1:
         print ('Ваша буква:')
     elif guess in alreadyGuessed:
         print ('Вы уже пробовали эту букву. Выберите другую')
     elif guess not in 'ёйцукенгшщзхъфывапролджэячсмитьбю' :
         print ('Пожалуйста, введите букву кириллицы')
     else:
         return guess

def playAgain () :
         print('Хотите попробовать еще раз ("Да" или "Нет")')
         return input () .lower() .startswith ('д')

print ('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord (words)
gameIsDone = False

while True:
          displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

          guess = getGuess (missedLetters+correctLetters)

          if guess in secretWord:
              correctLetters = correctLetters + guess

       foundAllLetters = True
       for i in range (len (secretWord)):
           if secretWord[i] not in correctLetters:
               foundAllLetters = False
               break
            if foundAllLetters:
                print ('Отлично! Было загадано слово "'+secretWord+'"! Вы победили')

                gameIsDone = True
        else:
              missedLetters = missedLetters + guess

            if len(missedLetters) == len(HANGMANPICS) -1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print('У Вас не осталось попыток!\nПосле '+srt(len(missedLetters))+' ошибок и '
                      +str(len(correctLetters))+'угаданных букв. Загаданное слово:'+secretWord+'"')
                gameIsDone = True

            if gameIsDone:
                if playAgain():
                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = gerRandomWord(words)
        else:
            break