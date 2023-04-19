"""
Given two strings, write a method to decide if one is a permutation of the other.

Permutation is defined as the two strings have the same characters with the same
frequency (number of appearances).

Example:
    Input: 'abcd', 'dcba'
    Output: True

Example:
    Input: 'abcd', 'dcdb'
    Output: False

ord('A')=65, order of the alphabet
chr(65)="A", character of the alphabet
"""


# Solution with time O(n logn)
def permutation_1(s, t):
    if len(s) != len(t):
        return False
    return ''.join(sorted(s)) == ''.join(sorted(t))


# Better solution with O(n)
def permutation_2(s, t):
    if len(s) != len(t):
        return False

    letters = [0] * 128
    s_list = [ord(i) for i in s]

    for i in s_list:
        letters[i] += 1  # Count the number of letters

    for i in t:
        ascii_order = ord(i)
        letters[ascii_order] -= 1
        if letters[ascii_order] < 0:
            return False

    return True


if __name__ == "__main__":
    s = 'abcd'
    t = 'dcba'
    print(permutation_1(s, t))
    print(permutation_2(s, t))


