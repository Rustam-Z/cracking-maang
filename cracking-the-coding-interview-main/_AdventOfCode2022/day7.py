import pathlib
import sys
from pprint import pprint

MAX_FOLDER_SIZE = 100000
MAX_DISK_SPACE = 70000000
UNUSED_SPACE_NEEDED = 30000000


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


def solution(data: list[str]):
    """Solution for part 1.

    Problem:
        Calculate the total size of each directory, find the directories with <= 100000.
        Then calculate the sum of their total sizes.

    Solution:
        $ cd - changes directory, if "cd .." then go up
        $ ls - lists files and subdirectories

    Let's imagine we have a hashmap to save a path and size

    if cd <DIR> then change the current_path, if cd .. then go back till previous /
    current_path = /d/

    if dir <DIR> then create a new path:
    / parent=None    size=14848514+8504156
    /a/ parent=/     size=29116+2557+62596
    /d/ parent=/     size=4060174+8033020+5626152+7214296
    /a/e/ parent=/d/ size=584

    Then in the end sum then again.
    """
    total_file_sizes_less_than_1000000 = 0
    fs = {}
    current_path = ['/']

    for line in data:
        if line.startswith('$ cd'):
            line_split = line.split()
            directory = line_split[2]

            if directory == '..':
                current_path.pop()
            elif directory == '/':
                current_path.clear()
                current_path.append('/')
            else:
                current_path.append(directory + '/')

        elif line.startswith('$ ls'):
            current_path_str = ''.join(current_path)
            parent_path_str = ''.join(current_path[:-1])

            fs[current_path_str] = {
                'parent': parent_path_str,
                'size': 0,
            }

        else:
            current_path_str = ''.join(current_path)

            if line.startswith('dir'):
                ...
            else:
                file_size, file_name = line.split()
                fs[current_path_str]['size'] += int(file_size)

    for path in reversed(fs):
        metadata = fs[path]
        if path == '/':
            continue
        else:
            fs[metadata['parent']]['size'] += metadata['size']

        size = metadata['size']
        if size <= MAX_FOLDER_SIZE:
            total_file_sizes_less_than_1000000 += size

    """Solution for part 2.
    
    MAX_DISK_SPACE = 70_000_000
    UNUSED_SPACE_NEEDED = 30_000_000
    TOTAL_SIZE_USED = 42_143_088
    
    Then, we need to remove 2143088 to install update.
    """
    space_used = fs['/']['size']
    need_to_remove = UNUSED_SPACE_NEEDED + space_used - MAX_DISK_SPACE
    smallest_file_size = float('inf')
    smallest_sizes_difference = float('inf')

    for metadata in fs.values():
        size = metadata['size']
        sizes_difference = size - need_to_remove  # Should be minimum positive.
        if 0 < sizes_difference < smallest_sizes_difference:
            smallest_sizes_difference = sizes_difference
            smallest_file_size = size

    return total_file_sizes_less_than_1000000, smallest_file_size


def solve(puzzle_input: str):
    # Solve the puzzle for the given input.
    # parse the given input
    data = parse(puzzle_input, 2)

    # get the solutions for each problem
    solution1, solution2 = solution(data)

    return solution1, solution2


if __name__ == "__main__":
    # print(sys.argv)
    for path in sys.argv[1:]:
        # print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
