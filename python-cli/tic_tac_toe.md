Tic-Tac-Toe teaches students how to decompose a larger program into functions while representing an entire game with a single list and simple algorithms.

A software architecture lesson. Not lists, which are used in Word Guess.
The lesson is to take a larger problem and decompose it into reusable pieces.

"Bad programmers worry about the code. Good programmers worry about data structures and their relationships." — Linus Torvalds

Objectives:
* **Functions**

  * Breaking a program into small, reusable pieces
  * Designing functions with a *single responsibility*
  * Parameters and return values

* **Program decomposition**

  * Separating input, game logic, rendering, and win detection
  * Reading a program by following high-level flow rather than every line

* **Lists as game state**

  * Representing an entire game board with a single list
  * Using indices to map positions to game squares

* **Coordinate mapping**

  * Translating a player's choice ("4") into a location on the board
  * Preparing students for 2D grids in Battleship and screen coordinates in p5

* **Algorithms**

  * Iterating over possible winning combinations
  * Searching data rather than hardcoding logic

* **State management**

  * Updating the board after each move
  * Alternating players
  * Detecting win, tie, or continue

---

Short and simple main loop that reads like pseudocode.

```python
get input
validate
update board
draw board
check win
change player
```
