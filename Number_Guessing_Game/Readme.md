# Number Guessing Game

A simple console-based **Number Guessing Game** built using Python. The program generates a random number and challenges the user to guess it within a limited number of attempts. The game provides hints after each guess and allows the player to replay without restarting the program.

---

## Features

* Random number generation between **1 and 100**
* Maximum of **10 valid attempts** per game
* Helpful hints: *Too high* or *Too low*
* Input validation (handles non-numeric and out-of-range input)
* Attempts are not wasted on invalid input
* Option to **play again** after each game

---

## How the Game Works

1. The system randomly selects a number between 1 and 100.
2. The user is prompted to guess the number.
3. After each valid guess, the program tells the user whether the guess is too high, too low, or correct.
4. The game continues until:

   * The user guesses the correct number, or
   * The user uses all 10 attempts.
5. After the game ends, the user can choose to play again or exit.

---

## Input Validation

The program ensures:

* Only numeric input is accepted.
* The guessed number must be within the range 1–100.
* Invalid input does **not** reduce the number of attempts.

This prevents crashes and improves user experience.

---

## Technologies Used

* Python 3
* Built-in `random` module

---

## How to Run the Program

1. Make sure Python 3 is installed on your system.
2. Save the program file (for example: `number_guessing_game.py`).
3. Open a terminal or command prompt.
4. Run the program using:

   ```
   python number_guessing_game.py
   ```

---

## Sample Output

```
Guess the number: 50
Too low
2 attempts used
8 attempts remaining
```

---

## Learning Outcomes

This project helps practice:

* Loops and conditional statements
* Random number generation
* Exception handling
* Input validation
* Program flow control

---

## Future Enhancements

* Difficulty levels (easy, medium, hard)
* Score tracking or best-attempt record
* Prevent repeated guesses
* Graphical user interface (GUI)

---


Enjoy playing the game and feel free to improve it further!
