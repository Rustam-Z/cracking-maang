import pathlib
import sys

MIDDLE_OF_THE_GRID = 16
START_ROW, START_COLUMN = MIDDLE_OF_THE_GRID, MIDDLE_OF_THE_GRID
DIRECTIONS = {
    'up': 'U',
    'right': 'R',
    'down': 'D',
    'left': 'L',
}


def part1(
        data: list,
        start_row: int = START_ROW,
        start_column: int = START_COLUMN
) -> int:
    """Solution for part 1.

    Problem:
        Given the direction, and number of steps to move.
        Only HEAD moves. And TAIL should go after HEAD. No distance diff should be between them.
        They can be placed in one cell also.
        Find the number of cells TAIL visits at least one.

    Solution:
        Simulate a 2D grid with 1000x1000 cells.
        H = Head. T = tail
        Place H and T in the middle [500][500].
        Create a set to save the cells, T visited. And in the end return the length of set.
    """
    tail_visited_cells = {
        (start_row, start_column),
    }

    head_row, head_column = start_row, start_column
    tail_row, tail_column = start_row, start_column

    for line in data:
        direction, number_of_steps = line.split()
        number_of_steps = int(number_of_steps)

        for _ in range(number_of_steps):
            head_row_prev, head_column_prev = head_row, head_column
            head_row, head_column = change_position(direction, head_row, head_column)
            # Check the distance with head and tail.
            is_touching_ = is_touching(head=(head_row, head_column),
                                       tail=(tail_row, tail_column))

            if not is_touching_:
                # Then change the position of tail to previous position of head.
                # And insert the tail's new position to visited set.
                tail_row, tail_column = head_row_prev, head_column_prev
                tail_visited_cells.add((tail_row, tail_column))

    return len(tail_visited_cells)


def part2(
        data: list,
        start_row: int = START_ROW,
        start_column: int = START_COLUMN
) -> int:
    """Solution for part 2.

    Problem: Now we have 9 numbers, and head. 9 is the tail.
    """
    tail_visited_cells = {
        (start_row, start_column),
    }

    positions = [(start_row, start_column), ] * 10  # 0 = head, 9 = tail.

    for line in data:
        direction, number_of_steps = line.split()
        number_of_steps = int(number_of_steps)

        for _ in range(number_of_steps):
            ...

    return len(tail_visited_cells)


def change_position(
        direction: str,
        head_row: int,
        head_column: int
) -> tuple[int, int]:
    if direction == DIRECTIONS['up']:
        head_row -= 1
    elif direction == DIRECTIONS['right']:
        head_column += 1
    elif direction == DIRECTIONS['down']:
        head_row += 1
    elif direction == DIRECTIONS['left']:
        head_column -= 1

    return head_row, head_column


def is_touching(head: tuple[int, int], tail: tuple[int, int]) -> bool:
    """
    If H is NOT in place of dots in pattern below or inplace of T, then return False.
    This function will be used to change the position of TAIL to previous position of HEAD.

    ...
    .T.
    ...

    """
    head_row, head_column = head
    tail_row, tail_column = tail

    head_possible_positions = (
        (tail_row - 1, tail_column - 1),
        (tail_row - 1, tail_column),
        (tail_row - 1, tail_column + 1),
        (tail_row, tail_column - 1),
        (tail_row, tail_column),
        (tail_row, tail_column + 1),
        (tail_row + 1, tail_column - 1),
        (tail_row + 1, tail_column),
        (tail_row + 1, tail_column + 1),
    )

    for row_position, column_position in head_possible_positions:
        if row_position == head_row and column_position == head_column:
            return True

    return False


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
