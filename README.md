# 8-Puzzle-Solver
8-puzzle is a simple puzzle game played on a 3x3 grid with 8 numbered and 1 empty slot.
A goal could be any configuration on the grid, however; often it is the ordered (ascending) numbers.

Aim of the project is to solve the 8-puzzle, using the [A*](https://en.wikipedia.org/wiki/A*_search_algorithm) heuristic search algorithm.
Two heuristic functions with different performance were used in the implementation; Manhattan distances and Gaschnig's heuristic.

The program solves an input puzzle configuration by providing a step-by-step pass to the input goal configuration. Note that the implementation 
is purely based on command line interface.

## Prerequisites
[Python version 3.8.5](https://www.python.org/downloads/release/python-385/) 
was used for development

## Installation
The project utilizes python built-in packages, hence no additional installations are required

## Getting Started
To run the project the below directory should be ensured (so that python scripts can import each other properly):
```
+-- puzzle
|   +-- __init__.py
|   +-- puzzle_base.py
|   +-- puzzle_heuristic.py
|   +-- puzzle_solver.py
```

To access the program, run the *puzzle/puzzle_solver.py* script:
```
>>> python puzzle_solver.py
```

The program will then request input start and goal configurations. In both cases, 
input should be a list of comma seperated numbers, the program will then convert them to 
2D 8-puzzle grids:

In case of empty input, the program will run based on default parameters. These 
can be changed on demand from the *sudoku_solver.py*.

## Details
- Author - Arastun Mammadli
- Completed as part of [ECM2423](http://emps.exeter.ac.uk/modules/ECM2423) coursework
- License - [MIT](LICENSE)
