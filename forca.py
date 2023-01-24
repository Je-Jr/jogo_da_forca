from os import system as stm
from random import randint
from words import all_words as aw

word = aw[randint(0, len(aw))]

flag = True
correct_guesses = ''
user_attempts = 0

while flag:
    user_guess = input('Digite uma letra: ')
    stm('cls')
    user_attempts += 1

    if len(user_guess) > 1:
        print('Digite apenas uma letra!')
        continue

    if user_guess in word:
        correct_guesses += user_guess

    secret_word = ''
    
    for letter in word:
        if letter in correct_guesses:
            secret_word += letter
        else:
            secret_word += '*'

    print(secret_word)

    if secret_word == word:
        print(
            f'PARABÉNS!\n'
            f'A palavra secreta era [{word}]\n'
            f'Quantidade de tentativas: {user_attempts}'
        )
        
        secret_word = ''
        user_attempts = 0
        flag = False
    