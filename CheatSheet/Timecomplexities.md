# Algorithms Time Complexity Cheatsheet

This document provides a quick reference for the time and space complexities of commonly used algorithms across different categories.

---

## Sorting Algorithms

| Algorithm        | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity |
|-------------------|----------------------|-------------------------|-----------------------|------------------|
| Bubble Sort      | \(O(n)\)            | \(O(n^2)\)              | \(O(n^2)\)            | \(O(1)\)         |
| Selection Sort   | \(O(n^2)\)          | \(O(n^2)\)              | \(O(n^2)\)            | \(O(1)\)         |
| Insertion Sort   | \(O(n)\)            | \(O(n^2)\)              | \(O(n^2)\)            | \(O(1)\)         |
| Merge Sort       | \(O(n \log n)\)     | \(O(n \log n)\)         | \(O(n \log n)\)       | \(O(n)\)         |
| Quick Sort       | \(O(n \log n)\)     | \(O(n \log n)\)         | \(O(n^2)\)            | \(O(\log n)\)*   |
| Heap Sort        | \(O(n \log n)\)     | \(O(n \log n)\)         | \(O(n \log n)\)       | \(O(1)\)         |
| Counting Sort    | \(O(n+k)\)          | \(O(n+k)\)              | \(O(n+k)\)            | \(O(n+k)\)       |
| Radix Sort       | \(O(nk)\)           | \(O(nk)\)               | \(O(nk)\)             | \(O(n+k)\)       |
| Bucket Sort      | \(O(n+k)\)          | \(O(n+k)\)              | \(O(n^2)\)            | \(O(n+k)\)       |

> **Note:** Space complexity of Quick Sort depends on recursion depth.

---

## Search Algorithms

| Algorithm            | Best Time Complexity | Average Time Complexity | Worst Time Complexity | Space Complexity |
|-----------------------|----------------------|-------------------------|-----------------------|------------------|
| Linear Search        | \(O(1)\)            | \(O(n)\)               | \(O(n)\)              | \(O(1)\)         |
| Binary Search        | \(O(1)\)            | \(O(\log n)\)          | \(O(\log n)\)         | \(O(1)\)         |
| Interpolation Search | \(O(\log \log n)\)  | \(O(\log \log n)\)      | \(O(n)\)              | \(O(1)\)         |

---

## Graph Algorithms

| Algorithm                        | Time Complexity         | Space Complexity |
|----------------------------------|-------------------------|------------------|
| Breadth-First Search (BFS)       | \(O(V + E)\)            | \(O(V)\)         |
| Depth-First Search (DFS)         | \(O(V + E)\)            | \(O(V)\)         |
| Dijkstra's Algorithm             | \(O((V + E) \log V)\)   | \(O(V + E)\)     |
| Bellman-Ford Algorithm           | \(O(VE)\)              | \(O(V)\)         |
| Floyd-Warshall Algorithm         | \(O(V^3)\)             | \(O(V^2)\)       |
| Prim’s Algorithm (Min-Heap)      | \(O((V + E) \log V)\)   | \(O(V + E)\)     |
| Kruskal’s Algorithm              | \(O(E \log E)\)        | \(O(V)\)         |
| Topological Sorting (DFS)        | \(O(V + E)\)            | \(O(V)\)         |

---

## Dynamic Programming

| Algorithm                        | Time Complexity         | Space Complexity |
|----------------------------------|-------------------------|------------------|
| Fibonacci Sequence (Recursive)  | \(O(2^n)\)             | \(O(n)\)         |
| Fibonacci Sequence (DP)         | \(O(n)\)               | \(O(1)\)         |
| Longest Common Subsequence       | \(O(m \times n)\)      | \(O(m \times n)\)|
| Longest Increasing Subsequence   | \(O(n^2)\), \(O(n \log n)\) | \(O(n)\)         |
| Knapsack Problem                 | \(O(n \times W)\)      | \(O(W)\)         |
| Matrix Chain Multiplication      | \(O(n^3)\)             | \(O(n^2)\)       |

---

## String Matching Algorithms

| Algorithm                        | Time Complexity         | Space Complexity |
|----------------------------------|-------------------------|------------------|
| Naive String Matching            | \(O(mn)\)              | \(O(1)\)         |
| KMP Algorithm                    | \(O(m + n)\)           | \(O(m)\)         |
| Rabin-Karp Algorithm             | \(O(m + n)\) (average) | \(O(1)\)         |
| Boyer-Moore Algorithm            | \(O(m + n)\)           | \(O(1)\)         |

---

## Tree and Heap Algorithms

| Algorithm                        | Time Complexity         | Space Complexity |
|----------------------------------|-------------------------|------------------|
| Binary Search Tree (Search/Insert/Delete) | \(O(h)\)*      | \(O(1)\)         |
| AVL Tree (Search/Insert/Delete)  | \(O(\log n)\)          | \(O(1)\)         |
| Segment Tree (Build)             | \(O(n)\)               | \(O(n)\)         |
| Segment Tree (Query/Update)      | \(O(\log n)\)          | \(O(\log n)\)    |
| Fenwick Tree (Build)             | \(O(n)\)               | \(O(n)\)         |
| Fenwick Tree (Query/Update)      | \(O(\log n)\)          | \(O(1)\)         |
| Heapify (Build Heap)             | \(O(n)\)               | \(O(1)\)         |
| Insert into Heap                 | \(O(\log n)\)          | \(O(1)\)         |
| Delete from Heap                 | \(O(\log n)\)          | \(O(1)\)         |

> **Note:** \(h\) is the height of the tree.

---

## Miscellaneous Algorithms

| Algorithm                        | Time Complexity         | Space Complexity |
|----------------------------------|-------------------------|------------------|
| Union-Find (Path Compression)    | \(O(\alpha(n))\)        | \(O(n)\)         |
| Fast Exponentiation              | \(O(\log n)\)           | \(O(\log n)\)    |
| Convex Hull (Graham's Scan)      | \(O(n \log n)\)         | \(O(n)\)         |
| Sieve of Eratosthenes            | \(O(n \log \log n)\)    | \(O(n)\)         |

---

Feel free to contribute or suggest improvements!
