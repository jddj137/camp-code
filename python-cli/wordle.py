import random
from collections import Counter
from string import ascii_lowercase

from wordle_bank import get_random_words

# Game configuration
WORD_LEN = 5
HARD_MODE = True


def validate_input(guess: list, secret: list) -> bool:
    if len(guess) != len(secret):
        return False
    for char in guess:
        if char not in ascii_lowercase:
            return False
    return True


def evaluate_guess(guess: list, secret: list, attempted: set) -> (list, set):
    remaining = dict(Counter(secret))
    feedback = ["X"] * WORD_LEN

    for i, char in enumerate(guess):
        if char == secret[i]:
            feedback[i] = "Y"
            remaining[char] = remaining[char] - 1

    for i, char in enumerate(guess):
        if feedback[i] == "Y":
            continue

        if char in remaining:
            if remaining[char] > 0:
                feedback[i] = "M"
                remaining[char] = remaining[char] - 1
        else:
            attempted.add(char)

    return (feedback, attempted)


if __name__ == "__main__":
    word_bank = get_random_words()

    # Game setup and state tracking
    secret = random.choice(word_bank)
    secret = list(secret.lower())

    prev_guess = [-1] * WORD_LEN
    prev_feedback = ["X"] * WORD_LEN
    attempted = set()

    # Main game loop
    while True:
        # Get input
        guess = input(f"Input {WORD_LEN} letters:\n")
        guess = list(guess.lower())

        # Validate input
        valid_input = validate_input(guess, secret)

        if not valid_input:
            print(f"Input must be {WORD_LEN} letters.")
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
                    print("Hard mode: Cannot swap correct letters!")
                    break
                elif fb == "M" and prev_guess[i] not in guess:
                    fair_play = False
                    print("Hard mode: Must reuse misplaced letters!")
                    break

        if not fair_play:
            continue

        # Evaluate guess
        feedback, attempted = evaluate_guess(guess, secret, attempted)

        print(f"\nAttempted: {''.join(sorted(attempted))}")
        print("".join(guess))
        print("".join(feedback) + "\n")

        prev_guess = guess
        prev_feedback = feedback
