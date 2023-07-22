"""
Problem: Sequences are separated by 2 new lines. Sum them each. And return max sum.
Input data: https://adventofcode.com/2022/day/1/input

Constraints:
    - No negative integers
"""


def sum_top_k_calories(k: int = 1) -> int:
    top_calories = [float('-inf')] * k  # This will work with any input.
    total_calories_for_one_elf = 0

    with open('data/day1.txt', 'r') as file:
        for line in file.readlines():
            if line == '\n':
                top_calories.append(total_calories_for_one_elf)
                top_calories.sort(reverse=True)  # Sorting items in reversed order. Needs optimization.
                top_calories.pop()  # Removing the smallest item.
                total_calories_for_one_elf = 0
            else:
                total_calories_for_one_elf += int(line)

    return sum(top_calories)


def main():
    solution1 = sum_top_k_calories(k=1)
    solution2 = sum_top_k_calories(k=3)

    print(solution1, solution2)


if __name__ == "__main__":
    main()
