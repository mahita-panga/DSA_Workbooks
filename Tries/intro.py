"""
Time Complexity:

Insertion: O(N) where N is the length of the word being inserted. This is because we have to iterate over each letter of the word to find its corresponding node or create a node accordingly.
Search: O(N) where N is the length of the word being searched for. This is because in Trie search we traverse over each letter for the word from the root, checking if the current node contains a node at the index of the next letter. This process repeats until we reach the end of the word or encounter a node without the next letter.
Prefix Search: O(N) where N is the length of the prefix being searched for. Similar to searching for words, in prefix search we also iterate over each letter of the word to find its corresponding node.
Space Complexity: O(N) where N is the total number of characters across all unique words inserted into the Trie. For each character in a word, a new node may need to be created leading to space proportional to the number of characters.

"""
class Node:
    def __init__(self):
        # Array to store links to child nodes,
        # each index represents a letter
        self.links = [None] * 26
        # Flag indicating if the node
        # marks the end of a word
        self.flag = False

    # Check if the node contains
    # a specific key (letter)
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None

    # Insert a new node with a specific
    # key (letter) into the Trie
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    # Get the node with a specific
    # key (letter) from the Trie
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]

    # Set the current node
    # as the end of a word
    def setEnd(self):
        self.flag = True

    # Check if the current node
    # marks the end of a word
    def isEnd(self):
        return self.flag


class Trie:
    def __init__(self):
        # Constructor to initialize the
        # Trie with an empty root node
        self.root = Node()

    # Inserts a word into the Trie
    # Time Complexity O(len), where len
    # is the length of the word
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # Create a new node for
                # the letter if not present
                node.put(ch, Node())
            # Move to the next node
            node = node.get(ch)
        # Mark the end of the word
        node.setEnd()

    # Returns if the word
    # is in the trie
    def search(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                # If a letter is not found,
                # the word is not in the Trie
                return False
            # Move to the next node
            node = node.get(ch)
        # Check if the last node
        # marks the end of a word
        return node.isEnd()

    # Returns if there is any word in the
    # trie that starts with the given prefix
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                # If a letter is not found, there is
                # no word with the given prefix
                return False
            # Move to the next node
            node = node.get(ch)
        # The prefix is found in the Trie
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
