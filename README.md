# Welcome to the Sudoku Solver🧩

_(this project is still a work in progress)_

This project implements a Sudoku puzzle solver in Python.
It uses backtracking recursion to efficiently fill in a Sudoku board.

## How It Works ✨

Empty spaces are represented by 0.
The algorithm recursively tries numbers 1-9 in empty cells.
It uses a validator function to ensure Sudoku rules are not violated:
Each row must contain the numbers 1–9 without repetition.
Each column must contain the numbers 1–9 without repetition.
Each 3×3 box must contain the numbers 1–9 without repetition.
If a number fits, it moves forward; if not, it backtracks and tries the next number.

## Files 📄

solver(b) → Solves the Sudoku board recursively using backtracking.
validator(b, pos, n) → Checks if placing a number n at pos is valid.
find_empty(b) → Finds the next empty spot (where 0 is found).
print_board(b) → Nicely prints the board with 3×3 box separations.
pprint → Pretty-prints the final solved board after solving.
