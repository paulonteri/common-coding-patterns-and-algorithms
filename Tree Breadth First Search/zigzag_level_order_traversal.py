"""
Zigzag Traversal:
Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right,
  then right to left for the next level and keep alternating in the same manner for the following levels.
"""
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# O(N) time | O(N) space
def traverse(root):
    result = []

    my_queue = [root]
    left_to_right = True
    while len(my_queue) > 0:

        level = deque([])
        level_size = len(my_queue)
        while level_size > 0:
            # remove node from my_queue
            node = my_queue.pop(0)
            if node.left:
                my_queue.append(node.left)
            if node.right:
                my_queue.append(node.right)

            # add to level's node values
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            level_size -= 1
        result.append(list(level))
        left_to_right = not left_to_right
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
