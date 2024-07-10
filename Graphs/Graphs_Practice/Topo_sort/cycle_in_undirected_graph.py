"""
from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = [0]*V
		q = deque()
		q.append(0)
		visited[0] = 1

		while len(q)!=0:
            curr = q.popleft()
            for i in adj[curr]:
                if visited[i] == 1:
                    return True

                if visited[i] != 1:
                    q.append(i)
                    visited[i] = 1

		return False


ISSUE with this code:
    This does not correctly handle the detection of cycles in an undirected graph.
    Specifically, the algorithm needs to ensure that it doesn't count a
    back edge to the parent node (from which it came) as a cycle.
    Additionally, the algorithm needs to start a BFS (or DFS) from every node
    to ensure that disconnected components are also checked for cycles.

"""

from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycleBFS(self, V: int, adj: List[List[int]]) -> bool:
        """
        BFS WAY TO CHECK FOR A CYCLE IN UNDIRECTED GRAPH
        """
        visited = [False] * V

        def bfs(start: int) -> bool:
            q = deque([(start, -1)])  # (current node, parent node)
            visited[start] = True

            while q:
                curr, parent = q.popleft()

                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((neighbor, curr))
                    elif neighbor != parent:   #if it is visited and it is not a parent then it means its a cycle
                        return True  # Cycle detected
            return False

        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True

        return False

    def isCycleDFS(self, V: int, adj: List[List[int]]) -> bool:
        """
        DFS WAY TO CHECK FOR A CYCLE IN UNDIRECTED GRAPH
        """
        visited = [0]*V

        def dfs(curr,parent,adj,visited):
            visited[curr] = 1
            for nbr in adj[curr]:
                if visited[nbr] == 0:
                    if dfs(nbr, curr, adj, visited):
                        return True
                elif nbr != parent: #if neighbour is visited and it is not a parent then it means its a cycle
                    return True
            return False

        for i in range(V):
                if not visited[i]:
                    if dfs(i, -1, adj, visited):
                        return True

        return False
