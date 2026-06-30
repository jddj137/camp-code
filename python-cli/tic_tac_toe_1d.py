from string import digits

# Game settings
PLAYER_1_NAME = "Whale"
PLAYER_2_NAME = "Bug"

# Emoji codes: https://unicode.org/emoji/charts/full-emoji-list.html
PLAYER_1_TOKEN = "\U0001f433"  # spouting whale
PLAYER_2_TOKEN = "\U0001f41b"  # bug


def print_grid(grid: list[str]) -> None:
    if len(grid) != 9:
        print("Error: Invalid game board!")
        return

    print("")
    print(grid[0] + " | " + grid[1] + " | " + grid[2])
    print("- - - - -")
    print(grid[3] + " | " + grid[4] + " | " + grid[5])
    print("- - - - -")
    print(grid[6] + " | " + grid[7] + " | " + grid[8])
    print("")


def check_win(grid: list[str]) -> bool:
    if len(grid) != 9:
        print("Error: Invalid game board!")

    wins = [
        # Horizontal wins
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # Vertical wins
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # Diagonal wins
        (0, 4, 8),
        (2, 4, 6),
    ]

    for i, j, k in wins:
        if grid[i] == grid[j] == grid[k]:
            return True
    return False


def next_player(curr_player: str) -> str:
    if curr_player == PLAYER_1_NAME:
        return PLAYER_2_NAME
    else:
        return PLAYER_1_NAME


# Note: This function could be replaced by a dictionary
def player_token(curr_player: str) -> str:
    if curr_player == PLAYER_1_NAME:
        return PLAYER_1_TOKEN
    else:
        return PLAYER_2_TOKEN


# Game setup and state tracking
game_board = list(digits)
game_board.remove("9")  # only need 0-8; 9 grid spaces

curr_player = PLAYER_1_NAME
move_count = 1

# Game intro
print(f"Welcome to Tic-Tac-Toe: {PLAYER_1_NAME} vs. {PLAYER_2_NAME}")
print("Simply pick the square number for where you want to play!")
print_grid(game_board)

# Main game loop
while True:
    # Get input
    move = input(f"{curr_player}'s turn: ")

    # Validate input
    if move not in game_board:
        print("Input must be an open square number!")
        continue

    # Put move on board
    game_board[int(move)] = player_token(curr_player)
    print_grid(game_board)

    # Check for win
    if move_count >= 5:  # Can't win until fifth move
        win = check_win(game_board)

        if win:
            print(f"{curr_player} wins!")
            break
        elif move_count == 9:  # Ninth move is the final move
            print(f"Tie! {PLAYER_1_NAME} and {PLAYER_2_NAME} live in peace!")
            break

    # Setup next round
    curr_player = next_player(curr_player)
    move_count = move_count + 1
