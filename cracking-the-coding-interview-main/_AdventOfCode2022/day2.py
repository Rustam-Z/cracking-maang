"""Rock Paper Scissors

In 1st column A for Rock, B for Paper, and C for Scissors.
In 2nd column X for Rock, Y for Paper, and Z for Scissors.

Single round score = shape you selected + outcome of the round.
Shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) .
Outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won.

Input: https://adventofcode.com/2022/day/2/input

What would your total score be if everything goes exactly according to your strategy guide?

Solution part 1:
    - 1st Player    To win      Draw      To lose
        A           Y ()        X ()      Z ()
        B           Z ()        Y ()      X ()
        C           X ()        Z ()      Y ()

Solution part 2:
    X means you need to lose,
    Y means you need to end the round in a draw,
    Z means you need to win.
   - 1st Player    To win        Draw      To lose
    A               Z (Y)        Y (X)      X (Z)
    B               Z (Z)        Y (Y)      X (X)
    C               Z (X)        Y (Z)      X (Y)

"""

FILE_PATH = 'data/day2.txt'

SELECTED_SHAPE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
OUTCOME_SCORE = {
    'won': 6,
    'draw': 3,
    'lost': 0,
}
STRATEGY_OVERALL_SCORE = {
    'A': {
        'X': OUTCOME_SCORE['draw'] + SELECTED_SHAPE_SCORE['X'],
        'Y': OUTCOME_SCORE['won'] + SELECTED_SHAPE_SCORE['Y'],
        'Z': OUTCOME_SCORE['lost'] + SELECTED_SHAPE_SCORE['Z'],
    },
    'B': {
        'X': OUTCOME_SCORE['lost'] + SELECTED_SHAPE_SCORE['X'],
        'Y': OUTCOME_SCORE['draw'] + SELECTED_SHAPE_SCORE['Y'],
        'Z': OUTCOME_SCORE['won'] + SELECTED_SHAPE_SCORE['Z'],
    },
    'C': {
        'X': OUTCOME_SCORE['won'] + SELECTED_SHAPE_SCORE['X'],
        'Y': OUTCOME_SCORE['lost'] + SELECTED_SHAPE_SCORE['Y'],
        'Z': OUTCOME_SCORE['draw'] + SELECTED_SHAPE_SCORE['Z'],
    },
}
STRATEGY_FOR_PART2 = {
    'A': {
        'X': STRATEGY_OVERALL_SCORE['A']['Z'],
        'Y': STRATEGY_OVERALL_SCORE['A']['X'],
        'Z': STRATEGY_OVERALL_SCORE['A']['Y'],
    },
    'B': {
        'X': STRATEGY_OVERALL_SCORE['B']['X'],
        'Y': STRATEGY_OVERALL_SCORE['B']['Y'],
        'Z': STRATEGY_OVERALL_SCORE['B']['Z'],
    },
    'C': {
        'X': STRATEGY_OVERALL_SCORE['C']['Y'],
        'Y': STRATEGY_OVERALL_SCORE['C']['Z'],
        'Z': STRATEGY_OVERALL_SCORE['C']['X'],
    },
}


def part1(path: str) -> int:
    my_total_score = 0

    with open(path) as file:
        for line in file.readlines():
            opponent_selection, my_selection = line.split()
            score = STRATEGY_OVERALL_SCORE[opponent_selection][my_selection]
            my_total_score += score

    return my_total_score


def part2(path: str) -> int:
    my_total_score = 0

    with open(path) as file:
        for line in file.readlines():
            opponent_selection, how_round_should_end = line.split()
            score = STRATEGY_FOR_PART2[opponent_selection][how_round_should_end]
            my_total_score += score

    return my_total_score


def main():
    solution1 = part1(FILE_PATH)
    solution2 = part2(FILE_PATH)

    print(solution1, solution2)


if __name__ == "__main__":
    main()
