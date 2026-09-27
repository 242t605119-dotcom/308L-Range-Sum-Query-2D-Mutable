# LeetCode 308 - Range Sum Query 2D - Mutable

## Problem Statement

Given a 2D matrix, support two operations:

* Update the value of a cell.
* Calculate the sum of all elements inside a rectangular region.

## Example

### Input

```text
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3)
update(3, 2, 2)
sumRegion(2, 1, 4, 3)
```

### Output

```text
8
10
```

## Approach

Use a **2D Fenwick Tree (Binary Indexed Tree)** to efficiently handle matrix updates and rectangular sum queries.

## Algorithm

1. Build a 2D Fenwick Tree from the matrix.
2. For an update, calculate the difference between the old and new values.
3. Update the Fenwick Tree with the difference.
4. Calculate prefix sums using the Fenwick Tree.
5. Use four prefix sums to calculate the required rectangle sum.

## Time Complexity

* Initialization: `O(m × n × log m × log n)`
* Update: `O(log m × log n)`
* Sum Query: `O(log m × log n)`

## Space Complexity

`O(m × n)`

## Key Concepts

* 2D Fenwick Tree
* Binary Indexed Tree
* Matrix
* Prefix Sum
* Range Query

## Language

Python

## LeetCode Details

* **Problem:** 308
* **Title:** Range Sum Query 2D - Mutable
* **Difficulty:** Hard

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`
