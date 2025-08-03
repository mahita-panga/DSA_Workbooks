-> Problems that require sequences of elements to meet criteria often utilize prefix sums.
-> Another mistake is assuming dynamic programming (DP) is always the right approach for optimization problems. When faced with minimization or maximization, our first instinct might be to reach for DP. However, before committing to it, we need to check the constraints. If the problem lacks overlapping subproblems or an optimal substructure, DP may not be a suitable choice. ---- IT COULD BE BINARY SEARCH TOO (ex. min time to repair cars)
  - look at the constraints of space to search in. dp is generally a matric, so if constraints are too huge, then it is computationally infeasible. Think of Binary search in such case.

  -> If problem feels like DP but has large constraints it is a binary search problem.
  -> Check if it is possible to break it in such a way as:
    -> can we figure out the lb and up of the search space for the answer we are looking forget
    -> formulate the logic either with greedy or heap or anything such that with this logic, we
    are able to reduce or inc the space bounds for the Search
