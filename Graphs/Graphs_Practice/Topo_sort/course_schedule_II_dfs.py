"""
GFG: https://www.geeksforgeeks.org/problems/course-schedule

Similar to LC COURSE SCHEDULE II, only thing is we need to return the courses order.

Intuition:  -> Check if cycle is present. If cycle return [].
            -> Cycle checked with the help of path_visited.
            -> Stack used to save the order of courses.
            -> We do a DFS traversal and if no cycle found by the end of that path,
            during backtracking, push the nodes to a stack
            -> After traversal, pop the stack and this the order in which courses should be taken.

"""

#User function Template for python3
from collections import defaultdict

class Solution:

    def dfs(self,curr_node,stack,visited,path_visited,adj):
        visited[curr_node] = 1
        path_visited[curr_node] = 1
        for i in adj[curr_node]:
            if visited[i] == 0 :
                if self.dfs(i,stack,visited,path_visited,adj):
                    return True
            elif path_visited[i] == 1:
                return True

        stack.append(curr_node)
        path_visited[curr_node]  = 0

    def findOrder(self, n, m, prerequisites):
        # Code here
        #Create an adjacency list
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        if len(m) == 0:
            return [i for i in range(n-1, -1, -1)] if n > 1 else [0]

        visited = [0]*n
        path_visited = [0] * n
        stack = []
        res = []
        for i in range(n):
            if visited[i] ==0:
                if self.dfs(i,stack,visited,path_visited,adj):
                    return []
        while stack:
            res.append(stack.pop())
        return res


#{
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)

def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []

        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])

        ob = Solution()

        res = ob.findOrder(n, m, prerequisites)

        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends
