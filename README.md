# Eagle Delivery: Project 1 starter

Project Introduction: This is a project featuring a delivery service using an agent that explores and learns the best/optimal delivery route between one building entrance to another. It plans with a known given map and learns how to navigate through repeated experience. 

Starter Code Written By: Dr. Yunting Yin
TODOs Completed By: Daniel Nguyen

## Requirements

Use Python 3.9+.

## What already works

```bash
python3 (or py) run_project.py show
python3 (or py) run_project.py search --algorithm bfs --start S --goal W
python3 (or py) run_project.py search --algorithm bfs --map maps/emu_detour.txt --start S --goal W
python3 (or py) run_project.py random --start S --goal W --seed 0
python3 (or py) examples/interaction_demo.py
python3 (or py) -m unittest tests.test_environment -v
```

## New run commands 

```bash
python3 (or py) run_project.py search --algorithm astar --start S --goal W
python3 (or py) run_project.py search --algorithm astar --map maps/emu_detour.txt --start S --goal W
python3 (or py) run_project.py train  --start S --goal W --output results/baseline_SW
python3 (or py) run_project.py train  --map maps/my_campus.txt 
python3 (or py) summarize_results.py results/baseline_SW
```

## Experiment setting(s)

```bash
python3 (or py) run_project.py train  --epsilon 0.05 (or any value) 
```

On `emu_campus.txt`, BFS from S to W should return path length **18** and **67**
expanded nodes, The path visualization uses `o`.
