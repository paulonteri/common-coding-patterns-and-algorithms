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
    if not root:
        return []

    allPaths = []
    # find paths recursively
    _path_finder(root, s, [], allPaths)
    return allPaths


def _path_finder(curr, s, curr_path, allPaths):
    if curr is None:
        return

    # # gives us eror solvalble by backtracking
    # curr_path.append(curr.val)
    # curr_path  += [curr.val]
    curr_path = curr_path + [curr.val]
    s = s - curr.val

    # if the current node is a leaf and subrating it from s will give you 0, we have found a path, save the current path
    if s == 0 and not curr.left and not curr.right:
        # add's empy list ??? when I use curr_path.append(curr.val)
        allPaths.append(curr_path)
        # allPaths.append(list(curr_path)) # use this instead when using curr_path.append(curr.val)

    else:
        # traverse the left & right sub-tree
        _path_finder(curr.left, s, curr_path, allPaths)
        _path_finder(curr.right, s, curr_path, allPaths)

    # # incase we use curr_path.append(curr.val) instead of curr_path = curr_path + [curr.val] above, we will have to backtrack
    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    # del curr_path[-1]


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
    sum2 = 18
    print("Tree paths with sum2 " + str(sum2) +
          ": " + str(find_paths(root, sum2)))


main()

"""
This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. There will be two differences:
    1. Every time we find a root-to-leaf path, we will store it in a list.
    2. We will traverse all paths and will not stop processing after finding the first path.
"""
