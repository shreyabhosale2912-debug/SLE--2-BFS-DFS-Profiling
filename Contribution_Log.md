# Contribution Log

## SLE-2: BFS vs DFS Performance Profiling

### Student Details

- **Name:** Shreya Bhosale
- **PRN:** 25UAM140
- **Program:** SY B.Tech CSE (AI & ML)

---

## Contributions

### 1. BFS and DFS Implementation
- Implemented Breadth-First Search (BFS) for maze solving.
- Implemented Depth-First Search (DFS) for maze solving.
- Used the same 5 × 5 maze for both algorithms.
- Defined the start node as `(0, 0)` and goal node as `(4, 4)`.

### 2. Performance Benchmarking
- Added execution-time measurement using `time.perf_counter()`.
- Executed BFS and DFS for 50,000 iterations.
- Calculated the average execution time.
- Counted the number of nodes expanded by each algorithm.
- Compared the path lengths produced by BFS and DFS.

### 3. Profiling
- Installed and used `py-spy` for performance profiling.
- Generated the profiling flame graph as `profile.svg`.
- Verified that the profiling completed with 0 errors.

### 4. Documentation
- Created `README.md`.
- Documented the problem statement, objective, algorithms, profiling method, results, analysis, and conclusion.
- Created this contribution log to document the work completed.

---

## Final Files

- `bfs_dfs.py` – BFS and DFS implementation
- `benchmark.py` – Performance benchmarking program
- `profile.svg` – Profiling flame graph
- `README.md` – Project documentation
- `Contribution_Log.md` – Contribution record