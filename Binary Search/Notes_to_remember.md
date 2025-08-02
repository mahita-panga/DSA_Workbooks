
# 🧠 Binary Search Patterns — Last-Minute Cheat Sheet

2 important variations while defining the search space — `right-exclusive [l, r)` and `inclusive [l, r]`.

## ✅ Pattern 1: Right-Exclusive `[l, r)`

### 🧾 Template:

```python
l, r = start, end  # r is exclusive
while l < r:
    mid = (l + r) // 2
    if condition(mid):
        r = mid
    else:
        l = mid + 1
return l
```

🧠 Use When:
	•	Searching on answer space (e.g., min/max satisfying condition).
	•	Want to avoid reevaluating mid after adjustment.
	•	Problem asks: “minimum/maximum value such that…”

📌 Example:

Problem: Find the minimum speed to arrive on time.
```python
def minSpeed(dist, hour):
    def time_needed(speed):
        return sum(math.ceil(d / speed) for d in dist)

    l, r = 1, 10**7 + 1
    while l < r:
        mid = (l + r) // 2
        if time_needed(mid) <= hour:
            r = mid
        else:
            l = mid + 1
    return l if time_needed(l) <= hour else -1
```

⸻

✅ Pattern 2: Inclusive [l, r]

🧾 Template:
```python
l, r = start, end  # r is inclusive
while l <= r:
    mid = (l + r) // 2
    if condition(mid):
        r = mid - 1
    else:
        l = mid + 1
return l
```

🧠 Use When:
	•	Looking for exact index/value.
	•	Need to evaluate both l and r.
	•	Classic sorted array search problems.

📌 Example:

Problem: Find exact target in sorted array
```python
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```

⸻

🔁 Summary

•	[l, r] -- while l <= r	-- inclusive	--- Index/value lookup
•	[l, r) -- while l < r	-- right-exclusive ---	Threshold/min-max type problems

⸻

⚠️ Gotchas & Tips
	•	In [l, r) pattern:
	•	Don’t forget r = mid (not r = mid - 1)
	•	Loop ends at l == r; l is the answer
	•	In [l, r] pattern:
	•	Loop runs while l <= r
	•	Use r = mid - 1 and l = mid + 1 to shrink

⸻

✍️ Final Thought

If the problem involves finding a boundary/threshold, reach for [l, r).

If it involves locating a specific value/index, go with [l, r].


*** NOTE:
  -> If problem feels like DP but has large constraints it is a binary search problem.
  -> Check if it is possible to break it in such a way as:
    -> can we figure out the lb and up of the search space for the answer we are looking forget
    -> formulate the logic either with greedy or heap or anything such that with this logic, we
    are able to reduce or inc the space bounds for the Search
