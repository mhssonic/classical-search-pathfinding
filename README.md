# Classical Search Algorithms for Grid Pathfinding

Interactive pathfinding demo that compares **uninformed** and **informed** search on a discrete grid world (Pygame UI themed as Kirby).

Built for *Introduction to Artificial Intelligence*, Amirkabir University of Technology (AUT).

## Highlights

- Implements BFS, DFS, Uniform-Cost Search, Greedy Best-First Search, and A\*
- Shared node / frontier abstractions for fair algorithm comparison
- Editable grid maps (`matriz.txt`) and a real-time visualization of explored paths
- Suitable resume line: *Implemented and visualized classical search algorithms (BFS, DFS, UCS, Greedy, A\*) for grid pathfinding*

## Algorithms

| Category | Method |
|----------|--------|
| Uninformed | Breadth-First Search, Depth-First Search, Uniform-Cost Search |
| Informed | Greedy Best-First Search, A\* Search |

## Tech stack

Python · NumPy · Pygame

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

Change the world layout by editing `matriz.txt`, then re-run.

## Repository layout

```
main.py           Entry point
interface.py      Pygame visualization
node.py           Search node / state helpers
matriz.txt        Grid map definition
algorithms/       BFS, DFS, UCS, Greedy, A*
images/ font/ music/
```

## Course

Introduction to Artificial Intelligence — Amirkabir University of Technology
