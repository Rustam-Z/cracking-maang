"""
Is Unique: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Time: O(n)
Space: O(1) because len(ASCII chars) = 128
"""


def is_unique(string):
    """
    :param string: string to check for uniqueness
    :return: True if string has all unique characters, False otherwise
    """
    if len(string) > 128:
        return False
    char_set = [False] * 128
    for char in string:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True
    return True


if __name__ == '__main__':
    print(is_unique('abcd'))
    print(is_unique('abcda'))