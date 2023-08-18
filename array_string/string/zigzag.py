"""
The string "LAYPZLISHIRING" is written in a zigzag pattern on a given number of rows like this:
L   Z   H   N
A P L S I I G
Y   I   R
And then read line by line: "LZHNAPLSIIGYIR"
"""


def solution(string: str, no_of_rows: int) -> str:
    """
    Algorithm:
        - Create a list of lists of size no_of_rows
        - Iterate over the string and append the characters to the list of lists
            - If we reach the first row, we need to go down
            - If we reach the last row, we need to go up
        - Iterate over the list of lists and join the characters

    Time complexity: O(n)
    Space complexity: O(n)
    """
    if no_of_rows == 1:
        return string

    zigzag = [[] for _ in range(no_of_rows)]
    row = 0
    going_down = True

    for char in string:
        zigzag[row].append(char)
        if row == 0:  # If we reach the first row, we need to go down
            going_down = True
        elif row == no_of_rows - 1:  # If we reach the last row, we need to go up
            going_down = False

        if going_down:
            row += 1
        else:
            row -= 1

    # Join list of lists
    for i in range(len(zigzag)):
        zigzag[i] = "".join(zigzag[i])

    return "".join(zigzag)


if __name__ == "__main__":
    string = "PAYPALISHIRING"
    assert brute_force(string, 3) == "PAHNAPLSIIGYIR"
    assert brute_force(string, 4) == "PINALSIGYAHRPI"
