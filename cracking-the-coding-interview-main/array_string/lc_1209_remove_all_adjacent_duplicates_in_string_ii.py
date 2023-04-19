"""
LeetCode: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

Problem: Given the string and k, remove k occurrences of the adjacent characters

Solution:
1. Use the stack (char, counter), append if chars are not the same, else change counter.
Time: O(n)
Space: O(n)

Solution:
1. Use bool to check if last time we didn't delete anything.
2. Generally we traverse till the end of string many times till we don't delete anything
Time: O(??)
Space: O(1)
"""


def removeDuplicates(s: str, k: int) -> str:
    is_last_deleted = True

    while is_last_deleted:
        char = s[0]
        counter = 1  # K tracker
        i = 1
        while i < len(s):
            if s[i] == char:
                counter += 1
                if counter == k:
                    # change string deeedbbcccbdaa
                    s = "".join([s[:i - k + 1], s[i + 1:]])
                    i -= k
                    break
            else:
                # start = i
                char = s[i]
                counter = 1

            if i == len(s) - 1:
                is_last_deleted = False

            i += 1

    return s


def new_solution_remove_duplicates(s: str, k: int) -> str:
    stack = []

    for c in s:
        if stack and stack[-1][0] == c:  # check if stack is not empty
            stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([c, 1])

    return ''.join(char * count for char, count in stack)


if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    print(removeDuplicates(s, k))
    print(new_solution_remove_duplicates(s, k))

