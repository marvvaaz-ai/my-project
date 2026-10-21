# TikTakTok

A two-player tic-tac-toe game played in the terminal.

Players take turns placing **X** and **O** on a 3×3 board. The first player to get three in a row — horizontally, vertically, or diagonally — wins. If the board fills with no winner, the game is a draw.

## Requirements

- Python 3

## How to play

From the project directory:

```bash
python tiktaktok.py
```

On each turn, enter a row and column as two numbers from 1 to 3, separated by a space. For example, `2 1` places a mark in the middle row, left column.

Invalid moves (out of range, occupied cells, or non-numeric input) are rejected and you are asked to try again.
