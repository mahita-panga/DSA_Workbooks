from collections import deque
class BFS_DFS_Solution:
    #Recursion call to implement depth-first search
    def dfs_recursion(self,curr_node):
        self.visited[curr_node] = 1
        self.dfs.append(curr_node)
        for i in self.adj[curr_node]:
            if self.visited[i] != 1:
                self.dfs_recursion(i)

    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        self.adj = adj
        self.dfs = []
        self.visited = [0]*V

        root_node = 0
        self.visited[root_node] = 1

        self.dfs_recursion(root_node)

        return self.dfs

    def bfsOfGraph(self,V,adj):
        visited = [0]*V
        bfs = []
        q = deque()

        root_node = 0
        q.appendleft(root_node)
        visited[root_node] = 1

        while len(q) != 0:
            curr_node = q.pop()
            bfs.append(curr_node)

            for i in adj[curr_node]:
                if visited[i] != 1:
                    q.appendleft(i)
                    visited[i] = 1
        return bfs

V = 5
adj = [[2,3,1] , [0], [0,4], [0], [2]]
print("GRAPH TRAVERSALS")
print(f"DFS {BFS_DFS_Solution().dfsOfGraph(V,adj)}")
print(f"BFS {BFS_DFS_Solution().bfsOfGraph(V,adj)}")
