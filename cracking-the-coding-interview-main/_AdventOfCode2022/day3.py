"""
The Elf that did the packing failed to follow this rule for **exactly one** item type per rucksack.
Divide the input line into two parts, find that discrepancy. Sum all of them and return the sum.
Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

Constraints:
    - Upper case and lower case letters should be handled differently.
"""


import pathlib
import sys
import string


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


def calculate_priority(char: str) -> int:
    total = 0
    if 'a' <= char <= 'z':
        total = -ord('z') + ord(char) + 26
    elif 'A' <= char <= 'Z':
        total = -ord('A') + ord(char) + 27

    return total


def part1(data: list):
    """Solution for part 1."""
    total = 0
    for line in data:
        first_part = set(line[:len(line)//2])
        second_part = set(line[len(line) // 2:])
        intersection = first_part.intersection(second_part)

        char = list(intersection)[0]
        total += calculate_priority(char)

    return total


def part2(data: list, number_of_groups: int = 3):
    """Solution for part 2."""
    def restore_letters(letters: dict) -> None:
        for letter in letters:
            letters[letter] = 0
        return None

    total = 0
    letters = {letter: 0 for letter in string.ascii_letters}

    for idx in range(0, len(data), number_of_groups):
        groups = data[idx:idx+number_of_groups]
        groups_set = [set(group) for group in groups]

        # If count is 3 for some char, then it is the intersection between groups.
        for group in groups_set:
            for char in group:
                letters[char] += 1
        for char, count in letters.items():
            if count == 3:
                total += calculate_priority(char)
                # print(">>>", char)
        # print(">>> check that we have only 1 char")
        restore_letters(letters)

    return total


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
