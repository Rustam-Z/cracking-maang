def spiral_traversal(matrix: list[list[int]]) -> list[int]:
    # O(N) time, where N is number of matrix
    # O(N) space for saving iteration result

    result = []
    start_row, end_row = 0, len(matrix) - 1
    start_col, end_col = 0, len(matrix[0]) - 1

    while start_row <= end_row and start_col <= end_col:

        # TOP
        for col in range(start_col, end_col + 1):  # Inclusively take last item, like 1 2 3 4
            result.append(matrix[start_row][col])

        # RIGHT
        for row in range(start_row + 1, end_row + 1):
            result.append(matrix[row][end_col])

        # DOWN
        if start_row < end_row:  # Because it is already added by TOP
            for col in range(end_col - 1, start_col - 1, -1):
                result.append(matrix[end_row][col])

        # LEFT
        if start_col < end_col:  # Because it is already added by RIGHT
            for row in range(end_row - 1, start_row, -1):
                result.append(matrix[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
traversal = spiral_traversal(matrix)
pass
