#!/usr/bin/python3
"""solves N-queens puzzle"""

import sys


def init_board(n):
    """Initializationt with 0's"""
    bod = []
    [bod.append([]) for j in range(n)]
    [row.append(' ') for j in range(n) for row in bod]
    return (bod)


def board_deepcopy(bod):
    """Return pcopy of a chessboard"""
    if isinstance(bod, list):
        return list(map(board_deepcopy, bod))
    return (bod)


def get_solution(bod):
    """Return lists representation of solved chessboard"""
    soltn = []
    for j in range(len(bod)):
        for k in range(len(bod)):
            if board[j][k] == "Q":
                soltn.append([j, k])
                break
    return (soltn)


def xout(bod, row, col):
    """X out spots on board"""
    # X out forward spots
    for j in range(col + 1, len(bod)):
        bod[row][j] = "x"
    # X out backwards spots
    for j in range(col - 1, -1, -1):
        bod[row][j] = "x"
    # X out spots below
    for k in range(row + 1, len(bod)):
        bod[k][col] = "x"
    # X out spots above
    for k in range(row - 1, -1, -1):
        bod[k][col] = "x"
    # X out spots diagonally down to the right
    j = col + 1
    for k in range(row + 1, len(bod)):
        if j >= len(bod):
            break
        bod[l][j] = "x"
        j += 1
    # X out spots diagonally up to the left
    j = col - 1
    for k in range(row - 1, -1, -1):
        if j < 0:
            break
        bod[k][j]
        j -= 1
    # X out spots diagonally up to the right
    j = col + 1
    for k in range(row - 1, -1, -1):
        if j >= len(bod):
            break
        bod[k][j] = "x"
        j += 1
    # X out spots diagonally down to the left
    j = col - 1
    for k in range(row + 1, len(bod)):
        if j < 0:
            break
        board[k][j] = "x"
        j -= 1


def recursive_solve(bod, row, queens, solutions):
    """Recursively solve puzzle"""
    if queens == len(bod):
        solutions.append(get_solution(board))
        return (solutions)

    for j in range(len(bod)):
        if board[row][j] == " ":
            tmp_board = board_deepcopy(bod)
            tmp_board[row][j] = "Q"
            xout(tmp_board, row, j)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bod = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for s in solutions:
        print(s)
