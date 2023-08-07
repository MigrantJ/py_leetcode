"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""

from typing_extensions import TypedDict

TrieNode = TypedDict("TrieNode", {"_end": bool})


class WordDictionary:
    def __init__(self):
        self.head: TrieNode = {"_end": False}

    def addWord(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr:
                curr[char] = {"_end": False}
            curr = curr[char]
        curr["_end"] = True

    def search(self, word: str) -> bool:
        def recur(node: TrieNode, partial: str) -> bool:
            if len(partial) == 0:
                # tail case, return whether this was the end of the word or not
                return node["_end"]

            chars = partial[0]
            if chars == ".":
                chars = node.keys()
            new_partial = "" if len(partial) == 1 else partial[1:]
            for c in chars:
                if c == "_end":
                    continue
                if c in node:
                    res = recur(node[c], new_partial)
                    if res is True:
                        return True
                else:
                    return False
            return False

        return recur(self.head, word)
