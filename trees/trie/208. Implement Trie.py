"""
Input
    ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
    [null, null, true, false, true, null, true]
Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True
"""
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_end = False  # Used to mark the end of a word. This is important for cases like "app" and "apple".

    def insert(self, word: str) -> None:
        curr = self
        for char in word:
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # return True
    print(trie.search("app"))      # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))      # return True
