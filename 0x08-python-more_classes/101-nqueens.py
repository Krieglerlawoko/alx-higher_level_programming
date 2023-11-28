#!/usr/bin/python3
"""Solution to the N-queens puzzle"""
import sys


def init_board(n):
    """Initialization"""
    bord = []
    [bord.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in board]
    return (bord)


def board_deepcopy(bord):
    """Return a deepcopy"""
    if isinstance(bord, list):
        return list(map(bord_deepcopy, bord))
    return (bord)


def get_solution(bord):
    """Return list of lists representation of solved chessboard"""
    soltn = []
    for b in range(len(bord)):
        for h in range(len(board)):
            if bord[r][c] == "Q":
                soltn.append([r, h])
                break
    return (soltn)


def xout(bord, row, col):
    """X on chessboard"""
    # X out forward
    for h in range(col + 1, len(bord)):
        bord[row][h] = "x"
    # X out backwards
    for h in range(col - 1, -1, -1):
        board[row][h] = "x"
    # X out all spots below
    for r in range(row + 1, len(bord)):
        bord[r][col] = "x"
    # X out all spots
    for r in range(row - 1, -1, -1):
        bord[r][col] = "x"
    # X out all spots diagonally
    h = col + 1
    for r in range(row + 1, len(bord)):
        if h >= len(bord):
            break
        bord[r][h] = "x"
        h += 1
    # X out all spots diagonally
    h = col - 1
    for r in range(row - 1, -1, -1):
        if h < 0:
            break
        bord[r][h]
        h -= 1
    # X out all spots diagonally
    h = col + 1
    for r in range(row - 1, -1, -1):
        if h >= len(bord):
            break
        bord[r][h] = "x"
        h += 1
    # X out all spots diagonally
    h = col - 1
    for r in range(row + 1, len(bord)):
        if h < 0:
            break
        board[r][h] = "x"
        h -= 1


def recursive_solve(bord, row, queens, solutions):
    """Recursively solve N-queens"""
    if queens == len(bord):
        soltns.append(get_soltn(bord))
        return (soltns)

    for h in range(len(bord)):
        if bord[row][h] == " ":
            tmp_bord = board_deepcopy(bord)
            tmp_bord[row][h] = "Q"
            xout(tmp_board, row, h)
            soltns = recursive_solve(tmp_bord, row + 1,
                                        queens + 1, soltns)

    return (soltns)


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

    bord = init_board(int(sys.argv[1]))
    soltns = recursive_solve(bord, 0, 0, [])
    for solution in soltns:
        print(solution)
