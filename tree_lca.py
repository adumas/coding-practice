
#        5
#      /    \
#     4      3
#   /  \    /  \
#  2    1  11   12
#
# LCA(4,11) = 5
# LCA(2,4)  = 4
# LCA(11,7) = None


# If I find both node, then the current node
# has to be the node being shared by both nodes.

# If I find only one node
# 	- other node does not exist.
# 	- other node is decendent.
# If I find neither, return None
# DO NOT EDIT
# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# DO NOT EDIT
# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if lst[i + 1] is not None and i + 1 < len(lst):
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root


def lca_tree(root, node_a, node_b):

    def traverse(node):
        if node is None:
            return None
        elif node.value == node_a:
            return node
    result = traverse(root)
    return result


def test_lca_tree(tree, node_a, node_b):
    print "====="
    print "testing " + str(tree)
    print "for node A: " + str(node_a) + " and node B: " + str(node_b)
    print "result: " + str(lca_tree(deserialize(tree), node_a, node_b))


test_tree = [5, 4, 3, 2, 1, 11, 12]
test_lca_tree(test_tree, 4, 11)
