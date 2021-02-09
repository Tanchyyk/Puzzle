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


def validate_column(board: list) -> bool:
    """
    Function check if columns of a board are built correctly.
    Return True if it is, False - if it is not.
    """
    for index in range(len(board[0])):
        for row in board:
            if row[index].isnumeric() and row.count(row[index]) > 1:
                return False
    return True


def validate_color(board: list) -> bool:
    """
    Function check if all blocks in one color have not the same numbers inside.
    """
    for i in range(1, len(board[0]) + 1):
        list_of_nums = []
        for row in board:
            if row[i - 1].isnumeric():
                list_of_nums.append(int(row[i - 1]))
        for element in board[-i]:
            if element.isnumeric():
                list_of_nums.append(int(element))
        if len(set(list_of_nums)) < len(list_of_nums):
            return False
    return True


board = [
 "****3****",
 "***12****",
 "**321****",
 "*1234****",
 "    69857",
 " 6  83  *",
 "3   7  **",
 "  8  2***",
 "  2  ****"
]
print(validate_board(board))
print(validate_color(board))
print(validate_row(board))
print(validate_column(board))