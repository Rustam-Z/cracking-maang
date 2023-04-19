"""
NOTE: You have to change the input file. Leave only operations that need to be performed.
    Please update STACKS with your input data.

[T] [V]                     [W]
[V] [C] [P] [D]             [B]
[J] [P] [R] [N] [B]         [Z]
[W] [Q] [D] [M] [T]     [L] [T]
[N] [J] [H] [B] [P] [T] [P] [L]
[R] [D] [F] [P] [R] [P] [R] [S] [G]
[M] [W] [J] [R] [V] [B] [J] [C] [S]
[S] [B] [B] [F] [H] [C] [B] [N] [L]
 1   2   3   4   5   6   7   8   9
"""

import pathlib
import sys
from copy import deepcopy


STACKS = {
    '1': ['S', 'M', 'R', 'N', 'W', 'J', 'V', 'T'],
    '2': ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V'],
    '3': ['B', 'J', 'F', 'H', 'D', 'R', 'P'],
    '4': ['F', 'R', 'P', 'B', 'M', 'N', 'D'],
    '5': ['H', 'V', 'R', 'P', 'T', 'B'],
    '6': ['C', 'B', 'P', 'T'],
    '7': ['B', 'J', 'R', 'P', 'L'],
    '8': ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W'],
    '9': ['L', 'S', 'G'],
}


def parse(puzzle_input: str, type: int = 1, seperator: str = "\n") -> list[str] | str:
    """Parses the string input, and return list if type is handled in code, otherwise returns original input.
    """
    if type == 1:
        return puzzle_input.split()
    elif type == 2:
        return puzzle_input.split(seperator)
    elif type == 3:
        return puzzle_input.strip().split(seperator)
    else:
        return puzzle_input


def part1(data: list, stacks: dict):
    """Solution for part 1."""

    for idx, step in enumerate(data):
        step = step.split()
        move, from_, to_ = step[1], step[3], step[5]

        # Logic for part 1
        for _ in range(int(move)):
            stacks[to_].append(stacks[from_].pop())

    head_of_stacks = [i[-1] for i in stacks.values()]

    return ''.join(head_of_stacks)


def part2(data: list, stacks: dict):
    """Solution for part 2."""

    for idx, step in enumerate(data):
        step = step.split()
        move, from_, to_ = int(step[1]), step[3], step[5]

        # Logic for part 2.
        stacks[to_].extend(stacks[from_][-move:])
        del stacks[from_][-move:]

    head_of_stacks = [i[-1] for i in stacks.values()]

    return ''.join(head_of_stacks)


def solve(puzzle_input: str):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)
    # get the solutions for each problem
    solution1 = part1(data, stacks=deepcopy(STACKS))
    solution2 = part2(data, stacks=deepcopy(STACKS))

    return solution1, solution2


if __name__ == "__main__":
    # print(sys.argv)
    for path in sys.argv[1:]:
        # print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
