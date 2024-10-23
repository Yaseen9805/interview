import random
print("Welcome to the Number guessing Game")
print("Im thinking of a number between 1 and 100")
diff = input("Choose a difficulty. Type 'easy' or 'hard':")
number=random.randint(1,100)
easy_guess=10
hard_guess=5
should_continue=True
while should_continue:
    if diff=='easy':

        print(f"You have {easy_guess} attempts remaining to guess the number.")
        user_guess=int(input("Make a guess:"))
        if user_guess==number:
            print(f"You got it! the answer was {number}")
            should_continue=False
        elif user_guess>number:
            print("Too high")
            print("guess again")
            easy_guess-=1
        elif user_guess<number:
            print("Too low")
            print("guess again")
            easy_guess-=1
        if easy_guess==0:
            print("out of guesses,you lose")
            should_continue=False

    elif diff=='hard':

        print(f"You have {hard_guess} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess:"))
        if user_guess == number:
            print(f"You got it! the answer was {number}")
            should_continue = False
        elif user_guess > number:
            print("Too high")
            print("guess again")
            hard_guess -= 1
        elif user_guess < number:
            print("Too low")
            print("guess again")
            hard_guess -= 1
        if hard_guess == 0:
            print("out of guesses,you lose")
            should_continue=False

    else:
        print("invalid ")
