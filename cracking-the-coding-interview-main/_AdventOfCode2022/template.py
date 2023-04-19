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


def part1(data: list):
    """Solution for part 1."""
    return 0


def part2(data: list):
    """Solution for part 2."""
    return 0


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
