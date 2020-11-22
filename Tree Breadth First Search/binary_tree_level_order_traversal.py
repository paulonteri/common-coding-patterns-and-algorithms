"""
Binary Tree Level Order Traversal:
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []

    my_queue = [root]
    while len(my_queue) > 0:

        nodes_at_level = []
        level_size = len(my_queue)
        while level_size > 0:
            # get the first item\
            node = my_queue.pop(0)

            # add node's children to queue
            if node.left:
                my_queue.append(node.left)

            if node.right:
                my_queue.append(node.right)

            nodes_at_level.append(node.val)
            level_size -= 1

        result.append(nodes_at_level)

    return result


def traverse2(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))
    print("Level order traversal2: " + str(traverse2(root)))


main()

"""
SOLUTION:
Since we need to traverse all nodes of each level before moving onto the next level,
 we can use the Breadth First Search (BFS) technique to solve this problem.
We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:
    1. Start by pushing the root node to the queue.
    2. Keep iterating until the queue is empty.
    3. In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes in the current level.
    4. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
    5. After removing each node from the queue, insert both of its children into the queue.
    6. If the queue is not empty, repeat from step 3 for the next level.
"""
