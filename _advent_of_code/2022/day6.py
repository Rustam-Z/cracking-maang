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


def solution(data: list, number_of_distinct_chars: int) -> int:
    """Solution for part 1 and 2."""
    number_of_chars = 0
    start = 0

    for idx in range(number_of_distinct_chars, len(data)):
        chars = set(data[start:idx])
        if len(chars) == number_of_distinct_chars:
            number_of_chars += number_of_distinct_chars
            break
        else:
            start += 1
            number_of_chars += 1

    return number_of_chars


def solve(puzzle_input: str):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, None)
    # get the solutions for each problem
    solution1 = solution(data, number_of_distinct_chars=4)
    solution2 = solution(data, number_of_distinct_chars=14)

    return solution1, solution2


if __name__ == "__main__":
    # print(sys.argv)
    for path in sys.argv[1:]:
        # print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
