"""
Given the array of words and the width of the line,
justify the text, so that each line has width characters
and is fully justified on both sides. And return string.
Each line should have max_width characters. You need just use spaces ' ' to fill the gaps.

Constrains and questions:
    - is it guaranteed that each work is shorter than max_width?
    - How we should place spaces to justify the text? (left, right, center) What is we have only one word in the line?
"""


def solution(words: list, max_width: int) -> str:
    """
    Algorithm:
        1. Iterate over words
        2. Check if we can add word to the line
        3. If we can't add word to the line, then justify the line and add to the result
        4. If we can add word to the line, then add word to the line
        5. Create another function that justifies the line

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def justify_line(line: list, max_width: int) -> str:
        """
        Algorithm:
            1. Calculate the number of spaces we need to add to the line
            2. Calculate the number of spaces we need to add to each gap
            3. Iterate over the line and add spaces to each gap
        """
        if len(line) == 1:
            return line[0] + ' ' * (max_width - len(line[0]))
        spaces = max_width - sum(len(word) for word in line)  # Number of spaces we need to add
        gaps = len(line) - 1  # Number of words, that have gaps between them.
        spaces_per_gap = spaces // gaps  # Number of spaces we need to add to each gap
        # extra_spaces = spaces % gaps  # Number of extra spaces we need to add to the gaps.
        justified_line = ''

        for i in range(len(line) - 1):
            justified_line += line[i] + ' ' * spaces_per_gap
            # if extra_spaces > 0:
            #     justified_line += ' '
            #     extra_spaces -= 1
            #
        justified_line += line[-1]

        return justified_line

    result = []
    line = []  # Keep track of each line
    for word in words:
        if len(' '.join(line)) + len(word) <= max_width:
            line.append(word)
        else:  # If we can't fit, we justify previous line and create new line
            result.append(justify_line(line, max_width))
            line = [word]
    if line:
        result.append(justify_line(line, max_width))

    return '\n'.join(result)


def main():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
    print(solution(words, max_width))

    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 14
    print(solution(words, max_width))


if __name__ == '__main__':
    main()
