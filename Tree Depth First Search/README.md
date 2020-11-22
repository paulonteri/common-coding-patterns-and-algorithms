# Depth First Search (DFS)

This pattern is based on the Depth First Search (DFS) technique to traverse a tree.

We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.
This also means that the space complexity of the algorithm will be O(H)O(H), where ‘H’ is the maximum height of the tree.

---

Note:
    - `stack` for **DFS**, imagine a vertical flow: seen earliest will be come for later
    - `queue` for **BFS**, horizontal flow
