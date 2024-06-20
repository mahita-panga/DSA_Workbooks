"""
LC 127: Word Ladder
A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Intuition:
    ->Bruteforce is take the word, step by step for every character coming, replace it with one of the 26 possibilities
   and see if that is the word in wordList. If found, we pick that word and do the same action again until we reach
   the end of word list
        - Eg: hit -> cog , wordlist = ["hot","dot","dog","lot","log","cog"]

    -> Other optimal approach is to use BFS technique where we traverse breadth wise by replacing
    each character with one of the 26 alphabets and see if the word being formed is there in the word list
    -> We track the words that are seen in word list in visited[] to ensure we dont keep traversing the
    the word changes again.
    -> Below is the approach:
        --> q.add((begin_word,1)) 1 here identifies the step/counter to track number of changes req to reach
        the endWord


"""
from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordlist: List[str]) -> int:
        wordList = set(wordlist)
        alphabets='abcdefghijklmnopqrstuvwxyz'


        q = deque()
        step = 1
        q.append((beginWord,step))
        visited = set([beginWord])

        while len(q)!=0:
            word,step = q.popleft()
            for i in range(len(word)):
                for c in alphabets:
                    next_word = word[:i]+c+word[i+1:]
                    if next_word == endWord:
                        if next_word in wordList:
                            return step+1
                        else:
                            return 0
                    if next_word in wordList and next_word not in visited:
                        q.append((next_word,step+1))
                        visited.add(next_word)
        return 0
