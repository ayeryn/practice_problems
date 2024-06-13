from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                continue
            elif (
                board[i][j] in rows[i]  # check row
                or board[i][j] in cols[j]  # check col
                or board[i][j] in squares[(i // 3, j // 3)]  # check 3x3
            ):
                return False
            rows[i].add(board[i][j])
            cols[j].add(board[i][j])
            squares[(i // 3, j // 3)].add(board[i][j])

    return True
