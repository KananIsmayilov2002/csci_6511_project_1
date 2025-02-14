# N-Puzzle Solver

## Overview

This repository contains a Python implementation of an N-Puzzle solver using the A* search algorithm. The N-Puzzle is a classic problem in artificial intelligence, consisting of a square grid with numbered tiles and a blank space. The goal is to rearrange the tiles from a given initial configuration to a desired target configuration by sliding tiles into the blank space.

This solver provides:

*   **A\* Search Implementation:**  An efficient search algorithm to find the optimal solution.
*   **Manhattan Distance Heuristic:**  A common and effective heuristic for estimating the distance to the goal state.
*   **Puzzle Generation:**  Functions to generate both initial and target puzzle states.
*   **Solvability Check:** Implicitly handles solvability by not finding a solution if the puzzle is unsolvable.
*   **Unit Tests:**  Comprehensive unit tests to ensure code correctness and robustness.

## Features

*   Reads puzzle configuration from a text file.
*   Calculates the Manhattan distance heuristic.
*   Generates valid neighbor puzzle states.
*   Solves the puzzle using A* search.
*   Prints the solution path (sequence of puzzle states).
*   Includes unit tests for all major functions.



### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/KananIsmayilov2002/csci_6511_project_1.git
    cd csci_6511_project_1
    ```


### Usage

1.  **Input file:**

    I have a text file (e.g., `n-puzzle.txt`) with the initial puzzle configuration. The file contains the puzzle state, with numbers separated by tabs or spaces, and rows separated by newlines. `0`  represents the blank tile.  For example:

    ```
    1   2   3
    4   0   6
    7   5   8
    ```

2.  **Run main code:**

    ```bash
    python n_puzzle_solver.py
    ```

    The script will read the puzzle from `n-puzzle.txt` (or you can modify the script to read from a different file), solve it, and print the solution path to the console.


## Code Structure

*   `n_puzzle_solver.py`: Contains the main logic for the N-Puzzle solver, including:
    *   `read_puzzle()`: Reads the puzzle configuration from a file.
    *   `find_blank()`: Finds the coordinates of the blank space.
    *   `calculate_manhattan_distance()`: Calculates the Manhattan distance heuristic.
    *   `generate_target_puzzle()`: Generates the target puzzle configuration.
    *   `get_neighbors()`: Generates possible neighbor puzzle states.
    *   `solve_n_puzzle()`: Solves the puzzle using A* search.
    *   `print_puzzle()`: Prints the puzzle configuration.
*   `test_n_puzzle_solver.py`: Contains the unit tests for the functions in `n_puzzle_solver.py`.

## Testing

To run the unit tests, execute the following command:

```bash
python -m unittest test_n_puzzle.py
