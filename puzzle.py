def validate_board(board: list) -> bool:
    if validate_row(board) and validate_column(board) and validate_color(board):
        return True
    return False


def validate_row(board: list) -> bool:
    for row in board:
        list_of_nums = []
        for el in row:
            if el.isnumeric():
                list_of_nums.append(int(el))
        if len(set(list_of_nums)) == len(list_of_nums):
            return True


def validate_column(board: list) -> bool:
    for index in range(len(board[0])):
        list_of_nums = []
        for row in board:
            if row[index].isnumeric():
                list_of_nums.append(int(row[index]))
        if len(set(list_of_nums)) != len(list_of_nums):
            return False
    return True


def validate_color(board: list) -> bool:
    for i in range(1, len(board[0]) + 1):
        list_of_nums = []
        for row in board:
            if row[i - 1].isnumeric():
                list_of_nums.append(int(row[i - 1]))
        for el in board[-i]:
            if el.isnumeric():
                list_of_nums.append(int(el))
        if len(set(list_of_nums)) != len(list_of_nums):
            return False
    return True


board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   6  **",
 "  8  2***",
 "  2  ****"
]

print(validate_board(board))