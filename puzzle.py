"""
https://github.com/Tanchyyk/Puzzle.git
"""


def validate_board(board: list) -> bool:
    """
    Function validate a board of a game.
    Return True if board is ready for the game, False - in other case.
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    if validate_row(board) and validate_column(board) and validate_color(board):
        return True
    return False


def validate_row(board: list) -> bool:
    """
    Function check if rows of a board are built correctly.
    Return True if it is, False - if it is not.
    """
    for row in board:
        for element in row:
            if element.isnumeric() and row.count(element) > 1:
                return False
            return True


def get_column(board: list) -> list:
    columns = []

    for i in range(len(board[0])):
        column = ""
        for row in board:
            column += row[i]
        columns.append(column)
    return columns


def validate_column(board: list) -> bool:
    """
    Function check if columns of a board are built correctly.
    Return True if it is, False - if it is not.
    """
    columns = get_column(board)

    if validate_row(columns):
        return True
    return False


def get_color(board: list) -> list:
    one_color = []
    columns = get_column(board)
    for i in range(len(board)):
        line = ""
        line += board[-i]
        line += columns[i]
        one_color.append(line)

    return one_color


def validate_color(board: list) -> bool:
    """
    Function check if all blocks in one color have not the same numbers inside.
    """
    one_color = get_color(board)
    if validate_row(one_color):
        return True
    return False


board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   9  **",
 "  8  2***",
 "  2  ****"
]
print(validate_board(board))
print(validate_color(board))
print(validate_row(board))
print(validate_column(board))