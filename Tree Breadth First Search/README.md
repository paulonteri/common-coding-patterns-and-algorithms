# Breadth First Search

This pattern is based on the Breadth First Search (BFS) technique to traverse a tree.

Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a **Queue** to keep track of all the nodes of a level before we jump onto the next level. This also means that the space complexity of the algorithm will be O(W)O(W), where ‘W’ is the maximum number of nodes on any level.

---

Note:
    - `stack` for **DFS**, imagine a vertical flow: seen earliest will be come for later
    - `queue` for **BFS**, horizontal flow
