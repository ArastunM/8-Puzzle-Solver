"""
    Contains the base code of the 8-puzzle structure
    Understands 8-puzzle logics (potential/possible moves)
"""

import copy

board_size = 9


def get_index(element, position):
    """
    :param element: element to search for
    :param position: board position to refer to
    :return: index of the element at given position
    """

    for row_idx in range(len(position)):
        for col_idx in range(len(position[row_idx])):
            if position[row_idx][col_idx] == element:
                return row_idx, col_idx
    return None


def make_move(from_idx, to_idx, position):
    """
    :param from_idx: index to move from
    :param to_idx: index to move to
    :param position: initial board position
    :return: position after the move
    """

    new_position = copy.deepcopy(position)
    temp = position[to_idx[0]][to_idx[1]]
    new_position[to_idx[0]][to_idx[1]] = position[from_idx[0]][from_idx[1]]
    new_position[from_idx[0]][from_idx[1]] = temp
    return new_position


def are_neighbours(idx1, idx2):
    """
    :return: true if given tile indexes are neighbours, false otherwise
    """
    return (idx1[0] == idx2[0] and abs(idx1[1] - idx2[1]) == 1) or \
           (idx1[1] == idx2[1] and abs(idx1[0] - idx2[0]) == 1)


def get_neighbours(position):
    """
    :param position: board position to refer to
    :return: list of neighbouring positions
    """

    neighbours = []
    empty_index = get_index(0, position)
    for row_idx in range(len(position)):
        for col_idx in range(len(position[row_idx])):
            if are_neighbours((row_idx, col_idx), empty_index):
                new_neighbour = make_move((row_idx,  col_idx), empty_index, position)
                neighbours.append(new_neighbour)
    return neighbours
