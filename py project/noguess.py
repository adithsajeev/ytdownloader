import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

    
print("-------------------------------")
print("WELCOME TO NUMBER GUESSING GAME")
print("-------------------------------")


while is_running:

    guess = input("Guess a number: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("The number    you have entered is out of range")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("May be Too high! or just high 😁 Try agian!")
        else:
            print(f"CORRECT!! the answer was {answer}")
            print(f"Number of guesses {guesses}")
     
print("-------------------------------")

    