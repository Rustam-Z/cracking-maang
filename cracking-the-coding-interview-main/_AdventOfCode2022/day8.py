import pathlib
import sys


def parse(puzzle_input: str, type: int = 1, seperator: str = "\n") -> list[str] | str:
    """Parses the string input, and return list if type is handled in code, otherwise returns original input.
    """

    # print(puzzle_input)
    if type == 1:
        return puzzle_input.split()
    elif type == 2:
        return puzzle_input.split(seperator)
    elif type == 3:
        return puzzle_input.strip().split(seperator)
    else:
        return puzzle_input


def part1(data: list) -> int:
    """Solution for part 1.
    """
    number_of_trees_visible = 0

    # Counting trees in the edge of grid.
    rows_length = len(data[0])
    columns_length = len(data)
    number_of_trees_visible += (2 * rows_length) + (columns_length - 2) * 2

    # Create a 2D matrix.
    matrix = create_matrix(data)

    for row in range(1, rows_length - 1):
        for column in range(1, columns_length - 1):
            tree_height = matrix[row][column]

            top = [c[column] for c in matrix[:row]]
            right = matrix[row][column+1:]
            down = [c[column] for c in matrix[row+1:]]
            left = matrix[row][:column]

            # print(tree_height, top, right, down, left)

            for direction in top, right, down, left:
                if tree_height > max(direction):
                    number_of_trees_visible += 1
                    break

    return number_of_trees_visible


def part2(data: list) -> int:
    """Solution for part 2."""
    scenic_score_max = float('-inf')

    # Create a 2D matrix.
    matrix = create_matrix(data)

    for row in range(1, len(matrix) - 1):
        for column in range(1, len(matrix[0]) - 1):
            tree_height = matrix[row][column]
            top, right, down, left = 0, 0, 0, 0

            for tree_column in reversed(matrix[:row]):
                near_tree_height = tree_column[column]
                top += 1
                if near_tree_height >= tree_height:
                    break

            for near_tree_height in matrix[row][column + 1:]:
                right += 1
                if near_tree_height >= tree_height:
                    break

            for tree_column in matrix[row + 1:]:
                near_tree_height = tree_column[column]
                down += 1
                if near_tree_height >= tree_height:
                    break

            for near_tree_height in reversed(matrix[row][:column]):
                left += 1
                if near_tree_height >= tree_height:
                    break

            scenic_score = top * right * down * left
            scenic_score_max = max(scenic_score_max, scenic_score)

    return scenic_score_max


def create_matrix(data: list[str]) -> list[list]:
    matrix = []
    for row in data:
        matrix.append(list(row))
    return matrix


def solve(puzzle_input: str):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # print(sys.argv)
    for path in sys.argv[1:]:
        # print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
