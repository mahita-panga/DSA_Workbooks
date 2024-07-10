"""
ALIEN DICTIONARY
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary.
Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case,
thus you may return any valid order and output will be 1 if the order of string returned by the
function is correct else 0 denoting incorrect string returned.

N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output:
1
Explanation:
Here order of characters is
'b', 'd', 'a', 'c' Note that words are sorted and in the given language "baa" comes before
"abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

INTUITION:
    -> The idea is to create a graph out of the characters in the strings and then do a topological sort[BFS -> indegree and queue]
    -> Steps to approach this problem is:
        -> Graph Initialization
            -> Adjacency list
            -> Efficient way is to have indegree initialized with zeroes for K nodes,
            instead of traversing every character in words
        -> Graph Construction
            -> Graph will be created by comparing adjancent words until we find a distinct character between them :
                (baa , abcd) -> this tells us b comes before a
                (abcd,abce) -> this tells us d comes before e
            -> CATCH HERE is while adding to the adjacency list,
            convert the character to its ASCII code and subtract it with ASCII code of 'a': This gives us the node value of this character in our graph.
               In python this is done via ord()
               ord('a') i.e. ASCII of a is 97, ord('b') is 98 and so on.
               So, while creating graph out of (baa,abcd):
                   we will compare b and a: <- b comes before a
                   so we add a to the adjancency list of b i.e. adj[b]={a} i.e in our way adj[1] = [0]
        -> Graph Traversal
            -> Use Kahn's algo to do topo sort. (Generate indegree array, add all indegree 0 to queue and traverse )
            -> In case cycle found( which would generally not be but if found i.e. len(result) < number of nodes), return False

        -> Result Order Mapping:
            -> For the result in toposort, generate the characters back using chr() in python by using
            chr(i + ord('a')) for every i in toposort



"""

from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        # code here
        adj = defaultdict(list)
        #in_degree = {char: 0 for word in alien_dict for char in word} #Time complexity : O(N*M)
        in_degree = [0]*K

        # Step 2: Build the graph
        for first, second in zip(alien_dict, alien_dict[1:]):
            for char1, char2 in zip(first, second):
                if char1 != char2:
                    adj[ord(char1)-ord('a')].append(ord(char2)-ord('a'))
                    in_degree[ord(char2)-ord('a')] += 1
                    break

        # Step 3: Topological sort using BFS
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in adj[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < len(in_degree):
            return ""  # Cycle detected

        return "".join([chr(i+ord('a')) for i in result])

N = 5
K = 5
dict = ["baa","abcd","abca","cab","cad"]
Solution().findOrder(dict,N,K)
"""
TIME COMPLEXITY:  O(N) (iterating through the list of words) + O(N) for toposort
SPACE: O(1)
"""
