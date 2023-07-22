def spiral_traverse(array):
    result = []
    start_row = 0
    end_row = len(array) - 1
    start_col = 0
    end_col = len(array[0]) - 1
    get_perimeter(array, start_row, end_row, start_col, end_col, result)
    return result


def get_perimeter(array, start_row, end_row, start_col, end_col, result):
    if start_row > end_row or start_col > end_col:
        return

    # TOP
    for col in range(start_col, end_col + 1):  # Inclusively take last item, like 1 2 3 4
        result.append(array[start_row][col])

    # RIGHT
    for row in range(start_row + 1, end_row + 1):
        result.append(array[row][end_col])

    # DOWN
    if start_row < end_row:  # Because it is already added by TOP
        for col in range(end_col - 1, start_col - 1, -1):
            result.append(array[end_row][col])

    # LEFT
    if start_col < end_col:  # Because it is already added by RIGHT
        for row in range(end_row - 1, start_row, -1):
            result.append(array[row][start_col])

    get_perimeter(array,
                  start_row + 1,
                  end_row - 1,
                  start_col + 1,
                  end_col - 1,
                  result)
