from collections import Counter
from random import choice
from string import digits

# from random import randint

# Game configuration
SECRET_LEN = 4
HARD_MODE = True

# Game setup and state tracking
secret = [choice(list(digits)) for i in range(SECRET_LEN)]
# secret = [str(randint(0, 9)) for i in range(SECRET_LEN)]

prev_guess = [-1] * SECRET_LEN
prev_feedback = ["X"] * SECRET_LEN

# Main game loop
while True:
    # Get input
    guess = input(f"Input {SECRET_LEN}-digit number:\n")
    guess = list(guess.lower())

    # Validate input
    valid_input = len(guess) == len(secret)

    for char in guess:
        if char not in digits:
            valid_input = False
            break

    if not valid_input:
        print(f"Input must be {SECRET_LEN}-digit number")
        continue

    if guess == secret:
        print("\nWinners always win!")
        break

    # Hard mode validation
    fair_play = True
    if HARD_MODE:
        for i, fb in enumerate(prev_feedback):
            if fb == "Y" and guess[i] != secret[i]:
                fair_play = False
                print("Hard mode: Cannot swap correct digits!")
                break
            elif fb == "M" and prev_guess[i] not in guess:
                fair_play = False
                print("Hard mode: Must reuse misplaced digits!")
                break

    if not fair_play:
        continue

    # Evaluate guess
    remaining = dict(Counter(secret))
    feedback = ["X"] * SECRET_LEN

    for i, digit in enumerate(guess):
        if digit == secret[i]:
            feedback[i] = "Y"
            remaining[digit] = remaining[digit] - 1

    for i, digit in enumerate(guess):
        if feedback[i] == "Y":
            continue

        if digit in remaining and remaining[digit] > 0:
            feedback[i] = "M"
            remaining[digit] = remaining[digit] - 1

    print("".join(feedback))

    prev_guess = guess
    prev_feedback = feedback
