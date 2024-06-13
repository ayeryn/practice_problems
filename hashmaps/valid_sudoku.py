def isValidSudoku(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        row_seen = set()
        col_seen = set()

        for j in range(len(board)):

            # check row
            if board[i][j] != "." and board[i][j] not in row_seen:
                row_seen.add(board[i][j])
            elif board[i][j] in row_seen:
                return False

            # check col
            if board[j][i] != "." and board[j][i] not in col_seen:
                col_seen.add(board[j][i])
            elif board[j][i] in col_seen:
                return False

    d = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for i in range(0, len(board), 3):
        for j in range(0, len(board), 3):

            # check 3x3
            seen = set()
            for x, y in d:
                if board[i + x][j + y] != "." and board[i + x][j + y] not in seen:
                    seen.add(board[i + x][j + y])
                elif board[i + x][j + y] in seen:
                    return False

    return True
