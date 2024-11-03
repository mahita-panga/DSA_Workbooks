"""
If there is no common prefix, return ''

Using a trie for fetching the longest common prefix among all words in the list
"""

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

    def search(self, word):
        curr = self.root
        prefix_len = 0

        for ch in word:
            if len(curr.children) != 1:
                return prefix_len
            prefix_len += 1
            curr = curr.children[ch]
        return prefix_len

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        prefix_len = float("inf")
        for word in strs:
            trie.addWord(word)
        for word in strs:
            prefix_len = min(prefix_len,trie.search(word))

        return strs[0][:prefix_len]
