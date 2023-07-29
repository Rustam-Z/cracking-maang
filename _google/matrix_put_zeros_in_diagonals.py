def put_zeros_in_square_matrix_diagonals(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)

    for r in range(n):
        for c in range(n):
            if r == c or r + c == n - 1:
                matrix[r][c] = 0

    return matrix


def _test_1():
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    expected_result = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert put_zeros_in_square_matrix_diagonals(matrix) == expected_result


if __name__ == '__main__':
    _test_1()
