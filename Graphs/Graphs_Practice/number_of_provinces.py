"""
LC #547: Number of provinces(directly/indirectly connected groups) in given graph.

Intuition:
    Traverse graph via dfs/bfs
    Whenever there is no connection,visited[i] at that nodes is 0.
    Traverse again from unconnected nodes and do it until visited[i] has all 1's
    No.of times bfs/dfs is called is number of provinces

Since, matrix is given, converting it into adjacency list and performing the traversals.

Time: O(N) + O(V+2E) : outer loop(number of times we need to run until visited is all 1's)
+ DFS

Space: O(2N) : auxillary stack space and visited array

"""
from typing import List

class Solution:
    def dfs_recursion(self,curr_node,dfs):
        dfs.append(curr_node)
        self.visited[curr_node] = 1
        for i in self.adj_list[curr_node]:
            if self.visited[i] != 1:
                self.dfs_recursion(i,dfs)

    def convert_to_adj_list(self, matrix):
        adj_list =[[] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and i!=j:
                    adj_list[i].append(j)
        return adj_list

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        root_node = 0
        dfs = []
        provinces = 0

        self.adj_list = self.convert_to_adj_list(isConnected)
        self.visited = [0]*len(self.adj_list)


        for i in range(len(self.visited)):
            if self.visited[i] == 0:
                provinces+=1
                self.dfs_recursion(i,dfs)

        return provinces

# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))
