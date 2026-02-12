

questions =("How many elemnents are in preodic table?: ",
            "Which animal lays the ;argest eggs?: ",
            "What is the most abudunta gas in the atmosphere?: ",
            "How many bones in the human body",
            "Which is the hottest planets in the solar system?: ")

options = (("A. 116","B. 117.","C. 118","D. 119"),
           ("A. Duck","B. hen","C. ostrich","D. elephanat"),
           ("A. hydrogen","B. nitrogen","C. oxygen","D. heilum"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mecury","B. venus","C. Mars","D. Earth"))

answers = ("C","C","C","A","B")

guesses = []

score = 0

question_num = 0


for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter  (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    question_num += 1

    score = int(score / len(questions) * 100)
    print(f"{score}%")