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
    """Solution for part 1.
    In how many assignment pairs does one range fully contain the other?
    Pairs consist of 2 elfs only.
    """
    total = 0
    starts = []
    ends = []

    for idx, pairs in enumerate(data):
        pairs_sep = pairs.split(',')
        for section in pairs_sep:
            section_assignment = section.split('-')
            starts.append(int(section_assignment[0]))
            ends.append(int(section_assignment[1]))

        # print(starts, ends)
        # print(">> check")

        # TODO: code works only for two elfs
        if (starts[0] <= starts[1] and ends[0] >= ends[1]) or \
                (starts[0] >= starts[1] and ends[0] <= ends[1]):
            total += 1

        starts.clear()
        ends.clear()

    return total


def part2(data: list):
    """Solution for part 2.
    Check if we have the intersection.
    """
    total = 0
    one_pair_assigned_ranges = []
    one_pair_intersection = set()

    for idx, pairs in enumerate(data):
        pairs_sep = pairs.split(',')
        for section in pairs_sep:
            elf_range = section.split('-')

            start = int(elf_range[0])
            end = int(elf_range[1])

            one_pair_assigned_ranges.append({i for i in range(start, end+1)})

        # print(elfs_pair_assigned_ranges)
        # print(">> check")

        # Find any intersection betwe en elfs in pair
        one_pair_intersection.clear()
        for idx in range(1, len(one_pair_assigned_ranges)):
            intersection = one_pair_assigned_ranges[idx-1].intersection(one_pair_assigned_ranges[idx])
            one_pair_intersection.update(intersection)

        if one_pair_intersection:
            total += 1

        one_pair_assigned_ranges.clear()

    return total


def solve(puzzle_input: str):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)
    # print(data)
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
