"""
    Contains the heuristics and A* algorithm of the 8-puzzle problem
    Used heuristics are: Manhattan distances and Gaschnig's heuristic
"""

from queue import PriorityQueue
from puzzle import puzzle_base


""" IMPLEMENTATION OF MANHATTAN DISTANCES """


def get_manhattan(idx1, idx2):
    """
    :return: the Manhattan distance between two tiles (idx1 and idx2)
    """

    return abs(idx1[0] - idx2[0]) + abs(idx1[1] - idx2[1])


def get_manhattan_sum(from_position, to_position):
    """
    :return: the Manhattan distance between two given board positions
    That is, sum of Manhattan distances of each tile from their position in the goal state
    """

    manhattan_sum = 0
    for element in range(1, puzzle_base.board_size):
        index1 = puzzle_base.get_index(element, from_position)
        index2 = puzzle_base.get_index(element, to_position)
        manhattan_sum += get_manhattan(index1, index2)
    return manhattan_sum


""" IMPLEMENTATION OF GASCHNIG'S HEURISTIC"""


def get_gaschnig(from_position, goal_position):
    """
    @:return: the Gaschnig's heuristic between two given board positions
    Gaschnig's heuristic is based on sum of number of tiles out of row,
                                        and number of tiles out of column
    """
    out_row = 0
    out_column = 0
    for element in range(1, puzzle_base.board_size):
        index1 = puzzle_base.get_index(element, from_position)
        index2 = puzzle_base.get_index(element, goal_position)

        if index1[0] != index2[0]: out_row += 1
        if index1[1] != index2[1]: out_column += 1
    return out_row + out_column


""" IMPLEMENTATION OF THE A* ALGORITHM """


def a_star(start, goal, heuristic):
    """
    :param start: starting state
    :param goal: final goal state
    :param heuristic: heuristic function to use (Manhattan or Gaschnig)
    :return: path from start to goal state
    """

    # current_node: tuple consisting of the start state and the path of start
    current_node = (start, [start])
    explored_states = []

    # priority_queue: used to store neighbours, and retrieve them based on priority
    count = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, count, current_node))

    while current_node[0] != goal or priority_queue.empty():
        # current_node is reassigned to the best node in priority queue
        current_node = priority_queue.get()[2]
        # cost is based on length of the path
        cost_so_far = len(current_node[1])
        explored_states.append(current_node[0])

        neighbours = puzzle_base.get_neighbours(current_node[0])
        for neighbour in neighbours:
            if neighbour not in explored_states:
                count += 1
                neighbour_path = puzzle_base.copy.deepcopy(current_node[1])
                neighbour_path.append(neighbour)

                #  priority is: cost so far + heuristic function result
                priority_queue.put((cost_so_far + heuristic(neighbour, goal),
                                    count, (neighbour, neighbour_path)))

    if current_node[0] != goal: return [], len(explored_states)
    # returning the solution path and total number of explored states
    return current_node[1], len(explored_states)
