import random


print('Welcome to the Number Guessing Game!')

input("Press Enter to start...")
print("""🎯 Number Guessing Game  Quick Rules
Guess the number chosen by the computer.

[1] The number is between 1 and 100.

[2] You get 7 tries to guess it.

[3] After each guess, you'll be told:

    🔼 Too high

    🔽 Too low

    ✅ Correct!

[4] You win if you guess it in time, else you lose.

[5] Only whole numbers are allowed.

""")

input("Press Enter to countinue...")

random_number = random.randint(1, 100)
tries = 7
while tries > 0:
    print("Number tries left:", tries)
    guess_number = int(input("Enter your guess: "))

    if (guess_number > random_number):
        print("Try Again! You guessed 🔼 Too high.")
        tries = tries-1
    elif (guess_number < random_number):
        print("Try Again! You guessed 🔽 Too low.")
        tries = tries-1
    else:
        print("Congratulations! Your guess is ✅ Correct!.")
        break

    if (tries == 0):
        print("Out of tries.Better Luck Next Time!")
        break
