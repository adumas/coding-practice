
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.


class Node():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def serialize(root):
    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        print current
        if current is not None:
            if current.left is not None or current.right is not None:
                queue.append(current.left)
                queue.append(current.right)
            result.append(current.value)
        else:
            result.append(None)

    if result[-1] is None:
        result.pop()

    return result


# [0,      1,    2,    3,     4]
# [root, left, right, left, right]


def deserialize(arr):
    root = Node(arr[0])
    queue = [root]
    while queue:


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
root.left.left.left = Node(0)


print serialize(root)
