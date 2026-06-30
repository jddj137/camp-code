import random

# Game settings
MIN = 0
MAX = 200

# Game setup
secret = random.randint(MIN, MAX)

# Game intro
print("Welcome to Number Guess!")
print(f"The computer chose a number between {MIN} and {MAX}.")
print("Can you guess it? \n")

# SOLUTION A: Check for correct answer each loop, i.e. sentinel-controlled loop
# Get user input
guess = input("Guess the secret number: ")  # guess is a string
guess = int(guess)  # guess is an integer

# Main game loop; check for win
while guess != secret:
    if guess < secret:
        print("Higher!")
    else:
        print("Lower!")

    # Get next guess
    guess = input("Guess the secret number: ")
    guess = int(guess)
print("Rise victorious young champion!")


# # SOLUTION B: Forever loop; break on success
# # Main game loop
# while True:
#     # Get user input
#     guess = int(input("Guess the secret number: "))

#     # Check for win
#     if guess == secret:
#         print("Rise victorious young champion!")
#         break
#     elif guess < secret:
#         print("Higher!")
#     else:
#         print("Lower!")
