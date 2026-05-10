# 🐍 Snake Water Gun Game (Python)

A simple command-line game built in Python where you play Snake, Water, Gun against the computer.

---

## Rules

| Your Pick | vs | Computer | Result |
| :--- | :---: | :--- | :--- |
| Snake | vs | Water | ✅ Snake wins (drinks the water) |
| Water | vs | Gun | ✅ Water wins (douses the gun) |
| Gun | vs | Snake | ✅ Gun wins (kills the snake) |
| Same | vs | Same | 🤝 Draw |


## 🎮 How to Play

Make sure you have Python 3 installed, then run:
```
python main.py
```
You'll be asked to enter:

0 for Snake
1 for Water
2 for Gun

The computer picks randomly. Your score is tracked across rounds until you choose to quit.
---


## How the Logic Works
The result is looked up from a 2D table where rows are the player's choice and columns are the computer's choice — no long if-else chains needed.
```
         Snake   Water   Gun
Snake  [  Draw,   Win,  Lose ]
Water  [  Lose,  Draw,   Win ]
Gun    [   Win,  Lose, Draw ]
```

---

## 🚀 Features

- Player vs Computer gameplay
- Score tracking (Wins, Losses, Draws)
- Loop to play multiple rounds
- Input validation

---

## 🧠 Concepts Used

- Python loops
- Dictionaries
- Lists (game matrix)
- Random module
- Conditional logic

---
