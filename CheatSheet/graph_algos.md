# Graph Algorithms Cheat Sheet

This guide provides an overview of essential graph algorithms and their implementations.

## Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. It can be used to detect cycles, traverse components, and more.

### **DFS Pseudocode**
```python
def dfs(graph, start, visited=set()):
    if start in visited:
        return
    visited.add(start)
    for neighbor in graph[start]:
        dfs(graph, neighbor, visited)
```
Use Cases
	•	Cycle detection in a directed/undirected graph
	•	Topological sort (modified DFS)
	•	Finding connected components

## Breadth-First Search (BFS)
explores all neighbors at the present depth before moving on to nodes at the next depth level. Ideal for finding the shortest path in unweighted graphs.
->Uses queue

### **BFS Pseudocode**
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## Multi-Source BFS
BFS from multiple sources simultaneously, often used when starting from multiple initial points.
->Means putting all the sources into the queue and exploring each path
```python
from collections import deque

def multi_source_bfs(graph, sources):
    visited = set(sources)
    queue = deque(sources)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```
Ex: Spread of infections, flood-filling algorithms

## Multiple Destinations Single Source
Finding the shortest path from a single source to multiple destinations, useful in scenarios with multiple targets.

Modification of BFS:  Run a regular BFS from the single source and stop when all destination nodes have been reached.

## Dijkstra’s Algorithm
shortest path from a source node to all other nodes in a weighted graph (only works with non-negative weights).
->Uses priority queue/ min heap to maintain the priorities
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
```
## Topological Sort
- orders nodes in a directed acyclic graph (DAG) where for any edge u -> v, u appears before v.
- BFS + indegree array.
### **Topological Sort with BFS (Kahn’s Algorithm)**
```python
from collections import deque, defaultdict

def topological_sort(graph, num_nodes):
    # Step 1: Initialize in-degree of all nodes
    in_degree = {i: 0 for i in range(num_nodes)}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Collect all nodes with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topological_order = []

    # Step 3: Process each node in queue
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        # Reduce the in-degree of neighboring nodes
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if there was a cycle
    if len(topological_order) != num_nodes:
        return []  # Cycle detected, no valid topological ordering

    return topological_order
```


## Union-Find (Disjoint Set Union - DSU)
Efficiently supports union and find operations for disjoint sets. Used for connected components and cycle detection.
```python
class DSU:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1]*(N)


    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x]) #PATH COMPRESSION
        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            if self.size[pu]<self.size[pv]: #Add smaller size node to larger size node
                self.parent[pu] = pv
                self.size[pv] += self.size[pu]
            else:
                self.parent[pv] = pu
                self.size[pu] += self.size[pv]
```
Usecases:
- Cycle detection in undirected graphs
-	Kruskal’s algorithm for MST

## Prim’s Algorithm (Minimum Spanning Tree)
MST -> Graph with N vertices and N-1 edges having minimum weight
Greedy algorithm that builds the MST by expanding the shortest edge from the existing tree.
->Uses minheap/PQ

```python
import heapq

def prims(graph, start):
    mst_cost = 0
    visited = set([start])
    min_heap = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]
    heapq.heapify(min_heap)

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst_cost += weight
            for next_neighbor, next_weight in graph[v].items():
                if next_neighbor not in visited:
                    heapq.heappush(min_heap, (next_weight, v, next_neighbor))

    return mst_cost
```
Best for dense graphs where E is large.

Ex:
Network design
Cable/roadway installation with minimal cost

## Kruskal’s Algorithm (Minimum Spanning Tree)
Greedy algorithm that builds the MST by adding edges in order of increasing weight, using Union-Find to avoid cycles.

```python
def kruskal(graph):
    edges = sorted(graph['edges'], key=lambda x: x[2])  # Sort edges by weight
    parent = {}
    rank = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    mst_cost = 0
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst_cost += weight

    return mst_cost
```
Best For: Sparse graphs, where E is small relative to V.

## Floyd-Warshall Algorithm (All-Pairs Shortest Path)
Dynamic programming algorithm for finding shortest paths between all pairs of nodes in a weighted graph.

```python
def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    for u in range(n):
        dist[u][u] = 0
    for u, v, weight in graph['edges']:
        dist[u][v] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```
Shortest paths in dense graphs
Graphs with negative weights (handles negative cycles)
