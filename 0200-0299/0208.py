"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""
from typing_extensions import TypedDict

TrieNode = TypedDict("TrieNode", {"_end": bool})


class Trie:
    def __init__(self):
        self.head: TrieNode = {"_end": False}

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr:
                curr[char] = {"_end": False}
            curr = curr[char]
        curr["_end"] = True

    def search(self, word: str) -> bool:
        curr = self.head
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return curr["_end"]

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True
