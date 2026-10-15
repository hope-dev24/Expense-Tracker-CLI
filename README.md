# Expense Tracker CLI

A command-line expense tracker built in Python. Lets you log expenses, view them, see totals, break spending down by category, and saves everything to a file so your data persists between runs.

## Features
- Add expenses with name, amount, and category
- View all logged expenses
- Get your total spending
- See spending broken down by category
- Clear all expenses (with confirmation)
- Save and load expenses from a file automatically

## Tech Used
- Python
- File I/O (reading/writing a plain text file for persistent storage)

## How to Run
1. Run the script: `python main.py`
2. Pick an option from the menu (1-6)

## What I Learned
Building this project taught me a lot about debugging real-world edge cases — including fixing a category-normalization bug, switching from `int()` to `float()` to correctly handle decimal amounts, and solving a data-parsing bug caused by using an unsafe delimiter when saving and loading expense data.
