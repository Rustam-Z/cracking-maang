"""
One Away

Edit operations on string: insert, remove, replace a char

MY SOLUTION:
- delete for longer string one by one, and check is str1==str2
- if len(str1)==len(str2) then delete char at each position for both strings, and check if strings are the same
    - or even better, found_diff=False, check one by one, if found found_diff=True, if found second time then retunr False
    - one_edit_replace() here it is

CTCI SOLUTION: #better
- Replacement
- Insertion & Removal merge, removal is the inverse of insertion
"""

def one_edit_way(first, second):
    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif len(first) + 1 == len(second):
        return one_edit_insert(first, second)
    elif len(first) - 1 == len(second):
        return one_edit_insert(second, first)

    return False # Meaning that length one string is 2 step longer

def one_edit_replace(s1, s2):
    found_diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_diff:
                return False
            found_diff = True
    return True

def one_edit_insert(s1, s2):
    """Check if we can insert a character into s1 to make s2, len(s2) > len(s1)"""
    index1 = 0
    index2 = 0

    while index2 < len(s2) and index1 < len(s1):
        """
        The code below works like this:
            ple
            pale

            1. equal
            2. not equal, then index2++, if not equal the second time, then "False" will be returned
        """
        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True

first = "pale"
second = "ple"
print(one_edit_way(first, second))