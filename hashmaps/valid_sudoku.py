from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(len(board)):
        for j in range(len(board)):
            # check row
            if board[i][j] != "." and board[i][j] not in rows[i]:
                rows[i].add(board[i][j])
            elif board[i][j] in rows[i]:
                return False

            # check col
            if board[i][j] != "." and board[i][j] not in cols[j]:
                cols[j].add(board[i][j])
            elif board[i][j] in cols[j]:
                return False

    d = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):
            for x, y in d:
                if (
                    board[i + x][j + y] != "."
                    and board[i + x][j + y] not in squares[(i, j)]
                ):
                    squares[(i, j)].add(board[i + x][j + y])
                elif board[i + x][j + y] in squares[(i, j)]:
                    return False

    return True
