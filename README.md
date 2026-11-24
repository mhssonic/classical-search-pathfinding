# Kirby — Find the Way

First project for **Introduction to AI** (Amirkabir University of Technology).

Kirby must reach the goal on a grid world using classic search algorithms. The UI is built with Pygame.

## Algorithms

| Type | Algorithms |
|------|------------|
| Uninformed | Breadth-First Search (BFS), Depth-First Search (DFS), Uniform-Cost Search |
| Informed | Greedy Best-First Search, A\* Search |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Edit `matriz.txt` to change the world layout (grid of cells Kirby can traverse).

## Project layout

```
.
├── main.py              # Entry point
├── interface.py         # Pygame UI
├── node.py              # Search node / state helpers
├── matriz.txt           # Grid world definition
├── algorithms/          # BFS, DFS, UCS, Greedy, A*
├── images/ font/ music/ # Assets
└── requirements.txt
```

## Requirements

- Python 3.9+
- `numpy`, `pygame` (see `requirements.txt`)
