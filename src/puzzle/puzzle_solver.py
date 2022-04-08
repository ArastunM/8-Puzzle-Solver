"""
    An implementation of A* search algorithm to solve the 8-puzzle problem
"""

import time
from puzzle import puzzle_heuristics
from puzzle import puzzle_base

# default start state (0 => empty tile)
default_start = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]
# default goal state
default_goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

config_error = "Incorrect Configuration Input!"
heuristic_error = "Incorrect Heuristic Function Choice!"


def convert_2d(list_1d):
    """
    :return: 3x3 2D form of the input array
    """

    list_2d = [list_1d[i:i+3] for i in range(0, len(list_1d), 3)]
    return list_2d


def interpret_input(input_str, default):
    """
    :param input_str: user input string
    :param default: default value, in case input was blank
    :return: interpreted 2D puzzle state
    """

    if input_str == "": return default
    input_str_list = input_str.split(",")

    input_list = []
    for string in input_str_list:
        try:
            input_list.append(int(string))
        except ValueError:
            print(config_error)
            return None

    if len(input_list) != puzzle_base.board_size:
        print(config_error)
        return None
    return convert_2d(input_list)


def input_request():
    """
    Requests user input from command line
    :return: start state, goal state and heuristic function to use
    """

    start = None
    goal = None
    heuristic_func = None

    while not (start and goal and heuristic_func):
        print("Enter starting configuration (empty for default): ")
        start = input()
        print("Enter goal configuration (empty for default): ")
        goal = input()
        print("Enter heuristic function (M - Manhattan, G - Gaschnig's heuristic): ")
        heuristic_func = input().upper().strip()

        # interpreting user input
        start = interpret_input(start, default_start)
        goal = interpret_input(goal, default_goal)

        if heuristic_func == 'M': heuristic_func = puzzle_heuristics.get_manhattan_sum
        elif heuristic_func == 'G': heuristic_func = puzzle_heuristics.get_gaschnig
        else:
            heuristic_func = None
            print(heuristic_error)

    return start, goal, heuristic_func


def print_position(board_position, message="CONFIGURATION:"):
    """
    prints out the given board_position
    """

    print(message, end="")
    for row_idx in range(len(board_position)):
        for col_idx in range(len(board_position[row_idx])):
            print(str(board_position[row_idx][col_idx]), end=" ")
        print()


def print_solution(solution, message="SOLUTION:"):
    """
    prints out the final search result
    :param solution: list of steps
    :param message: starting message
    """

    print(message)
    if len(solution) == 0: print("NO SOLUTION FOUND")
    else:
        step_count = 0
        for step in solution:
            print("STEP " + str(step_count) + ": ")
            print_position(step, "\0")
            # separating steps
            print("---------")
            step_count += 1


def main():
    print("WELCOME TO 8-PUZZLE SOLVER")
    start, goal, heuristic_func = input_request()
    print_position(start, "\nSTART CONFIGURATION:\n")
    print_position(goal, "GOAL CONFIGURATION:\n")

    start_time = time.time()  # starting the time
    result, iterations = puzzle_heuristics.a_star(start, goal, heuristic_func)
    print_solution(result, "\nSOLUTION (" + str(len(result) - 1) + " moves):")
    print("<<< Solved in %s seconds and %s iterations >>>" % (time.time() - start_time, iterations))


if __name__ == '__main__':
    main()
    exit(0)
