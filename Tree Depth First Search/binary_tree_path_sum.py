"""
Binary Tree Path Sum
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(N) time | O(N) space
def has_path(root, s):
    if root is None:
        return False

    s -= root.val

    # found required sum
    if s == 0:
        # is leaf
        if not root.left and not root.right:
            return True
        else:
            return False

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path(root.left, s) or has_path(root.right, s)


def has_path2(root, s):
    if root is None:
        return False

    # if the current node is a leaf and its value is equal to the sum, we've found a path
    if root.val == s and root.left is None and root.right is None:
        return True

    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    return has_path(root.left, s - root.val) or has_path(root.right, s - root.val)


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path2(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))
    print("Tree has path: " + str(has_path2(root, 16)))


main()

"""
SOLUTION:
has_path2:
As we are trying to search for a root-to-leaf path, we can use the Depth First Search (DFS) technique to solve this problem.
To recursively traverse a binary tree in a DFS fashion,
 we can start from the root and at every step, make two recursive calls one for the left and one for the right child.

Here are the steps for our Binary Tree Path Sum problem:
1. Start DFS with the root of the tree.
2. If the current node is not a leaf node, do two things:
    - Subtract the value of the current node from the given number to get a new sum => S = S - node.value
    - Make two recursive calls for both the children of the current node with the new number calculated in the previous step.
3. At every step, see if the current node being visited is a leaf node and if its value is equal to the given number ‘S’.
    If both these conditions are true, we have found the required root-to-leaf path, therefore return true.
4. If the current node is a leaf but its value is not equal to the given number ‘S’, return false.
"""
