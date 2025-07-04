import random
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_choosen):
    if level_choosen.upper() == "EASY":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
print("let's think a number between 1 to 50")
answer = random.randint(1,50)
level = input("choose the level ... type 'easy' or 'hard' : ")
attempt = set_difficulty(level)
def check_answer(guessed_number,answer,attempts):
    if guessed_number < answer:
        print("your guess is to low")
        return attempts-1
    elif guessed_number > answer:
        print("your guess is to high")
        return attempts -1
    else :
        print(f"your guess is right ... the answer is {answer}")
def game():
    print("let me think a number between 1 to 50 ")
    guess_number = 0
    while guess_number != answer:
        print(f"ypu have {attempt} attempts remaining to guess the number ...")
        guess_number = int(input("enetr your number"))
        attempts = check_answer(guess_number,answer,attempt)
        if attempt == 0:
            print("your are out of guesses ... loss game")
            return
        elif guess_number != answer:
            print("guess number")
game()
        
    



