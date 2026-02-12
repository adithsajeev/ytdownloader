import random
import time
import os
import sys


heart2 = """
      *****       *****
    *********   *********
  ************* *************
  ***************************
   *************************
     *********************
       *****************
         *************
           *********
             *****
               *

""" 

lowest_num = 1
highest_num = 100
answer = 7 #random.randint(lowest_num, highest_num)
guesses = 0
x = "16"
y = "2.9"
is_running = True
code = "love"
text = "I LOVE YOU KUNJOOSEE💖💖"
width = 40

imp_dates = {
    7 : "Its your roll number bby",
    16: "Its our anniversary day",
    50: "Half century",
    71: "Its my roll numberrr"
}

while True:
    guess = input("Enter your guess 🤔: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess in imp_dates:
            print()
            print(imp_dates[guess])

        if guess > highest_num or guess < lowest_num:
            print("Guess the the number in the range")

        elif guess > answer:
            print("answer = Too high")
        elif guess < answer:
            print("answer = Too low")
        else:
            print(f"Your answer is correct {answer} ")
            print(f"The number of guess you have taken {guesses}")
            print()
            break
    else:
        print("Pottathi correct number kodthe")

print()
print("\O HO Ig that was a easy question don't worry let me make it tuf🥱/")

print("Guess the secret key to enter my heart ❤️")
while True:
    
    key = input("ENTER THE KEY: ")

    if key == str(answer):
        print("Ammadi you found it 😘 Arada paranje kunjinu bhudhi illa enn ehh ehh ")
        break
    else:
        print("Pottathi avaleee angott alogich nokkk 🤔")
        print()

print()     
print()     
print("Appo ni paranju varunne ninak \n"
      "payagara bhudhi ane enn ane  \n"
        "seri akki therame")

while True:
    print()
    date = input("When is our anniversary(mention the date): ")

    if date == (x):
        print("---------THAKKUDUU😚😚😚💕---------")
        break
    else:
        print("NO MORE GAMES BYE 😠😡😤")
        sys.exit()
    
    print()
while True:
    print()
    date2 = input("How long have we been together?(year.date) ")

    if date2 == str(y):

        print("You are my bbyyy Ummmaa")

        while True:   
            os.system("cls" if os.name == "nt" else "clear")
            print(heart2)
            time.sleep(1)

            stop = input("Enter q to stop: ")
            if stop.lower()== "q":
             break
        break
    else:
        print("KOLAAAAAMMMMM kolaam poyi kankk koott")

print("Its time for the wish😊")
print()

code = input("Enter the word[love]: ")      
if code.lower() == ("love"):
   print()
   print("")
else:
    print("Enter the correct word")