# Q10. Let's create a "Number Guessing Game". Given a secret number (already
# decided by you), write a program that asks the user to guess it and prints:

# . "Too high" if the guess is above the number

# "Too low" if the guess is below
#  "Correct!"

# *if the guess matches

import random

secret_num = random.randint(1,100)
print("Secret num is: ", secret_num)


count = 0

while True:
    guess = int(input("Guess the num between 1 to 100 : "))
    count += 1

    if (guess > secret_num):
        print("Too high")
    elif (guess < secret_num) :
        print("Too low")
    else:
        print("\nCongrats your guess was correct " , "\nyour number of attempts = " , count ) 
        break   

