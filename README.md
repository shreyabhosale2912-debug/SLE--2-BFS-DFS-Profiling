# SLE-2: BFS vs DFS Performance Profiling

## Course

02AML204 – Introduction to Artificial Intelligence

## Student Details

- **Name:** Shreya Bhosale
- **PRN:** 25UAM140
- **Program:** SY B.Tech CSE (AI & ML)

## Problem Statement

To implement Breadth-First Search (BFS) and Depth-First Search (DFS) on the same maze and compare their practical performance using execution time, number of nodes expanded, and path length.

## Objective

- Implement BFS and DFS for maze solving.
- Find a path from the start node to the goal node.
- Compare the execution time of BFS and DFS.
- Compare the number of nodes expanded by both algorithms.
- Analyze the practical performance of both algorithms.

## Maze Used

A 5 × 5 maze grid was used.

- `0` = Path
- `1` = Wall
- **Start:** `(0, 0)`
- **Goal:** `(4, 4)`

Both BFS and DFS were tested using the same maze, start point, and goal point.

## Algorithms Used

### 1. Breadth-First Search (BFS)

BFS explores the maze level by level using a queue.

It follows the **FIFO (First In, First Out)** principle.

For an unweighted maze, BFS can find the shortest path.

### 2. Depth-First Search (DFS)

DFS explores one path deeply before backtracking.

It uses a stack and follows the **LIFO (Last In, First Out)** principle.

DFS can find a path, but the path is not necessarily the shortest in a general maze.

## Profiling Method

The performance was measured using:

- Python `time.perf_counter()` for execution time.
- 50,000 iterations for BFS and DFS.
- Execution time was measured in milliseconds.
- Number of expanded nodes was counted during the search.
- `py-spy` was used to generate the profiling flame graph.

## Results

The profiling run produced the following results:

| Metric | BFS | DFS |
|---|---:|---:|
| Average Time (ms) | 0.025739 | 0.013439 |
| Nodes Expanded | 17 | 9 |
| Path Length | 9 | 9 |

## Analysis

- BFS expanded 17 nodes in this particular maze.
- DFS expanded 9 nodes in this particular maze.
- Both algorithms found a path of length 9.
- The measured execution time was lower for DFS in this particular run.
- Execution time can vary between runs depending on the computer and system activity.

## Profiling Output

The profiling flame graph generated using `py-spy` is available in:

`profile.svg`

## Files

- `bfs_dfs.py` – BFS and DFS maze implementation
- `benchmark.py` – Performance benchmarking code
- `profile.svg` – Profiling flame graph
- `README.md` – Project documentation

## Conclusion

BFS and DFS were successfully implemented and tested on the same maze. In this experiment, both algorithms found a path of length 9. DFS expanded fewer nodes and had lower measured execution time in the profiling run, while BFS provides shortest-path guarantees for unweighted graphs.