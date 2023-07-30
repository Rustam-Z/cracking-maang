"""
https://leetcode.com/problems/partition-labels

Problem: You are given a string s. We want to partition the string into as many parts as possible so that each letter
appears in at most one part.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Solution:
    - Use hashmap to store the last index of each char.
    - However, the inner chars may come after the last index of the see char.
      For example, in "abccaddbeffe", the minimum first partition is "abccaddb". Because we have second b after second a.
      So, idea: process the last letter, use max.
"""


def partitionLabels(S):
    last_occurence = {char: index for index, char in enumerate(s)}
    j = last_break = 0
    result = []

    for index, char in enumerate(s):
        j = max(j, last_occurence[char])   # In case of abccaddbeffe, use abccaddb. Because we have second b after second a.

        if index == j:  # Means we find the end of break
            result.append(index - last_break + 1)  # Append index of break
            last_break = index + 1

    return result


if __name__ == "__main__":
    assert partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partitionLabels("abccaddbeffe") == [8, 6]
    assert partitionLabels("eccbbbbdec") == [10]
