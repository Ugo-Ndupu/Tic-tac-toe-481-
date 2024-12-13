# Tic-Tac-Toe AI

This is a simple command-line Tic-Tac-Toe game featuring an AI opponent implemented using the **Minimax algorithm with Alpha-Beta pruning**. The AI provides optimal moves and ensures competitive gameplay.

## Table of Contents

1. [Features](#features)
2. [How to Play](#how-to-play)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Overview](#code-overview)
6. [Technologies Used](#technologies-used)

---

## Features

- **Play Tic-Tac-Toe** on a 3x3 board.
- **Human vs. AI** gameplay.
- AI makes **optimal moves** using the Minimax algorithm.
- Supports **Alpha-Beta pruning** to optimize performance.
- Command-line interface for simplicity.

---

## How to Play

1. The game starts by asking you to choose your symbol (`X` or `O`).
2. Enter your moves by specifying the **row and column indices** (0-based).
3. The AI will respond with its move.
4. The game continues until:
   - A player wins, or
   - The board is full (resulting in a draw).

### Example Input

```
Do you want to be X or O? X
Players turn. Enter row and column (0-2):
0 0
```

---

## Installation

1. **Download or clone** the repository:

   ```bash
   git clone https://github.com/Ugo-Ndupu/Tic-tac-toe-481-.git
   cd Tic-tac-toe-481-
   ```

2. Ensure you have **Python 3** installed:

   ```bash
   python --version
   ```

---

## Usage

Run the script using the following command:

```bash
python Tic-Tac-Toe.py
```

---

## Code Overview

### Key Functions

- **`print_board(board)`**: Displays the current state of the board.
- **`is_winner(board, player)`**: Checks if the specified player has won.
- **`is_full(board)`**: Checks if the board is full.
- **`get_empty_cells(board)`**: Returns a list of empty cells.
- **`minimax(board, depth, is_maximizing, ai_player, human_player, alpha, beta)`**: Implements the Minimax algorithm with Alpha-Beta pruning.
- **`best_move(board, ai_player, human_player)`**: Determines the best move for the AI.

### Game Flow

1. **Player selects symbol** (`X` or `O`).
2. **Turns alternate** between the player and AI.
3. The game ends when there’s a winner or a draw.

---

## Technologies Used

- **Python 3**
- **Minimax Algorithm**
- **Alpha-Beta Pruning**

---
