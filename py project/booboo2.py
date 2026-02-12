import random
import time
import os
import sys


lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
x = "16"
y = "2.9"
text = "I LOVE YOU KUNJOOSEE💖💖"
width = 40

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

def type_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

imp_dates = {
    7 : "🎉Its your roll number bby 🎉",
    16: "🥳 Its our anniversary day 💕",
    50: "🏆 Half century celebration 💖",
    71: "🎉 Its my roll number 😁"
}


while True:
    print("🔔FOR BETTER EXPERIENCE PLEASE MAKE THE TERMINAL FULL SCREEN🔔")
    print()
    guess = input("Enter your guess 🤔 (1-100): ")


    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess in imp_dates:
            type_print(imp_dates[guess])

        if guess > highest_num or guess < lowest_num:
            type_print("🚫 Stay inside the range mandu  (1 - 100)")

        elif guess > answer:
            type_print("📈 Too highhhh madam ji Try smaller!", 0.02)
        elif guess < answer:
            type_print("📉 Too lowww kuttyyy 🥺 Try bigger!", 0.02)
        else:
            type_print(f"🎉 Hasthala vastha ⚡ Correct answer is {answer} 😘")
            print()
            break
    else:
        type_print(" Ayyoo thats not even a number pottathi 😑🤦‍♂️")

print()
type_print(" Guess the secret key to unlock my heart 🔐❤️")
while True:
    key = input("ENTER THE KEY: ")
    if key == str(answer):
        type_print("🎉 Ammbbadi you found it 😘 Arada paranje nta kunjinu bhudhi illa enn ehh ehh ")
        break
    else:
        type_print("🤦‍♂️  ETh nadakkilla 😑 🙊 (Hasthala vastha)")


print()     
type_print("Appo ni paranju varunne ninak payagara bhudhi ane enn ane seri akki therame 🤼")

while True:
    date = input("When is our anniversary (mention the date): ")
    if date == x:
        type_print("---------THAKKUDUU😚😚😚💕---------")
        break
    else:
        type_print("😤😡 Wrong answer! Access denied ❌💔 Byeeee!")
        sys.exit()
    
while True:
    date2 = input("How long have we been together? (year.months eg:1.4): ")
    if date2 == str(y):
        type_print("🥰 You are my bbyyy Ummmaaaaa 💋💖💞")

        
        while True:   
            os.system("cls" if os.name == "nt" else "clear")
            print(heart2)
            print("\nPress 'q' to get moree love 💌💗🫶")
            time.sleep(0.5)

            # Stop check
            stop = input()
            if stop.lower() == "q":
                break
        break
    else:
        type_print("😑 KOLAAAAAMMMMM 💀 Go calculate properlyyy daaa ➕ ➖ ➗✖️")


type_print("✨ Its time for the final wishhhhhh 😊💖✨", 0.07)
type_print("💖💞💘💗💌💕💘💖💝💞💗💘💖💌 \n"
           "💖💞💘💗💌💕💘💖💝💞💗💘💖💌", 0.02)

code = input("Enter the word [love] to get the message: ")      
if code.strip().lower() == "love":
    type_print("🥰❤️💖💞💘 Yay! You unlocked the full love surprise \n"
                "💝💌💗 \n"                    
                " 💘💘Kunjooseee Happy valentines day!!💘💘 \n"
                " \n"
                "💝 LET US BE ABLE TO CLEBRATE EVERY COMING VALANTIES DAY TOGETHER 🫂🫂🫂😚😚💕 \n"
                " 💗💌💕I Love you soo much bbyyyyyy💗💌💕\n"
                " ummmmmaa\n"
                " ummmmmaa\n"
                " ummmmmaa\n"
                " ummmmmaa\n"
                " ummmmmaa\n"
                " Thakkuduu aaa nteee--------nta pon🥹🫂\n"
                " Dhoree ayi poyi allagil nta pon inu nthagilum medich theramayirunu 🥺 \n"
                " \n"
                " \n"
                "🐣🐣🐣🐣🐣 MY BBYYYYY 🐣🐣🐣🐣🐣 \n"
                " \n"
                " ummmmmaaaa, ether umma thannalm mathi avilla nta poninu 🫦\n"
                " \n"
                " 💖HAPPY VALANTINES DAY💖\n", 0.05)
else:
    type_print("🚫 Wrong word 🚫  Type LOVE correctly 😤")
