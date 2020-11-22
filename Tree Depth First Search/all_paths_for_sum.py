"""
All Paths for a Sum:
Given a binary tree and a number ‘S’,
 find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, s):
    allPaths = []
    # find paths recursively
    _path_finder(root, s, [], allPaths)
    return allPaths


def _path_finder(curr_node, required_sum, current_path, allPaths):
    if curr_node is None:
        return

    current_path.append(curr_node.val)  # add the current node to the path
    required_sum -= curr_node.val

    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if required_sum == 0 and not curr_node.left and not curr_node.right:
        # print(type(current_path))
        # print(current_path)
        # allPaths.append(current_path) # add's empy list ???
        allPaths.append(list(current_path))

    else:
        # traverse the left & right sub-tree
        _path_finder(curr_node.left, required_sum, current_path, allPaths)
        _path_finder(curr_node.right, required_sum, current_path, allPaths)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del current_path[-1]


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()

"""
This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. There will be two differences:
    1. Every time we find a root-to-leaf path, we will store it in a list.
    2. We will traverse all paths and will not stop processing after finding the first path.
"""
