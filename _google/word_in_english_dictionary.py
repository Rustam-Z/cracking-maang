"""

"""
from collections import defaultdict


# assuming we have Trie implementation of dictionary

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False


def solve(allowed, words):
    res = []

    # Create trie
    root = Trie()
    for word in words:
        curr = root
        for char in word:
            curr = curr.children[char]
        curr.is_end = True

    # Find words
    def dfs(curr, b):
        if curr.is_end and len(b) >= 4:
            res.append(''.join(b))
        for child in curr.children:
            if child in allowed:
                b.append(child)
                dfs(curr.children[child], b)
                b.pop()

    dfs(root, [])
    return res


if __name__ == "__main__":
    allowed, words = "teoplam", ["team", "tap", "yahoo", "google"]
    print(solve(allowed, words))  # ['team']
