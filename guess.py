# Это игра по угадыванию чисел.
import random

guesses_taken = 0
print('Привет! Как тебя зовут?')
my_name = input()

number = random.randint(1, 20)
print('Что ж, ' + my_name + ', я загадываю число от 1 до 20.')

for guesses_taken in range(6):
    print('Попробуй угадать.') # Четыре пробела перед именем функции print
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Твое число слишком маленькое.')
    if guess > number:
        print('Твое число слишком большое.')
    if guess == number:
        break

if guess == number:
    guesse_taken = str(guesses_taken + 1)
    print('Отлично, ' + my_name + '! Ты справился за ' + guesses_taken + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадала число ' + number + '.')
