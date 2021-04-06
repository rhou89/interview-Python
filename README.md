# Data Structure
## Linear (one to one)
- Array or ordered array
- Stack (First In Last Out) (DFS)
- Queue (First In First Out) (BFS)
  - Double-ended queue
  - Blocking queue (wait for a time) or non-blocking queue
- [Linked list](https://blog.csdn.net/tianzhaixing2013/article/details/22717581)
  - Singly linked list
  - Circular linked list
  - Doubly linked list

## Tree (one to n)
- Binary Tree
  - [Traversal](https://en.wikipedia.org/wiki/Tree_traversal): Pre-order (NLR); In-order (LNR); Post-order (RNL)
  - [Binary search tree](https://blog.csdn.net/sysu_arui/article/details/7892593)
    - Segment tree
  - Self-balancing binary search tree
    - Red–black tree
    - Splay tree
    - AVL tree
    - (Multiway tree) B/B+/2-3/2-3-4 Tree
  - [Huffman Tree (optimal prefix code)](https://blog.csdn.net/qingdujun/article/details/54093419)
- Trie-trees
- Heap (priority queue and complete binary tree, can be realized using array)
  - min heap; max heap
- Hash Table (Know about python implementation and complexity)
  - Collision resolution
    - Separate chaining: dynamic array or linked list
    - Open addressing: linear/non-linear probing; double hashing
- [Disjoint set](https://zh.wikipedia.org/wiki/并查集)
  
## Graphs (n to n)
- Storage: Adjacency list; Adjacency matrix; Objects and pointers
- [Minimum spanning tree](https://blog.csdn.net/luoshixian099/article/details/51908175)
  - Kruskal (Edge)
  - Prime (Vertex)
- [Shortest path problem](https://blog.csdn.net/qibofang/article/details/51594673
)
  - Dijkstra
  - Floyd
- [Critical path method](https://www.cnblogs.com/jsgnadsj/p/3432820.html)
  - [Topological sorting](https://blog.csdn.net/lisonglisonglisong/article/details/45543451) (AOE: Activity On Edge Network, vertex: event)
  - Compare earliest start and latest start

# Algorithms
- Dynamic programming
  - Shortest Path
  - [Longest common subsequence](https://blog.csdn.net/chengonghao/article/details/51913108)
  - [0-1 Backpack](https://blog.csdn.net/chengonghao/article/details/51915753)
  - [Longest increasing subsequence](https://blog.csdn.net/s448312891/article/details/80318746)
- Greedy algorithm
- Recursion and backtracking
- Divide-and-conquer algorithm
- Proof by exhaustion
  - Search (BFS; DFS)

# Others
- [Sorting](https://www.cnblogs.com/onepixel/p/7674659.html)
  - Bubble (Compare neighbors)
  - Selection (Find the minimum)
  - Insertion or radix (Find the correct position to insert)
  - Merge
  - Quick Sort
  - Heap
- [String](https://www.cnblogs.com/gaochundong/p/string_matching.html)
  - Naive String Matching Algorithm
  - KMP
- NP-complete problems
  - TSP or Knapsack problem
  
## Reference
- [程序员必须掌握哪些算法？](https://www.zhihu.com/question/23148377)
