from BinaryTreeMaker import TreeMaker, Node


t = TreeMaker()
root = Node(1)
root = t.levelOrderBuilder([1,2,3, 4, 5, 6, 7],root, 0, 7)

from collections import deque
def levelOrderPrint(root):
    if not root:
        return []
    res = []
    current = deque()
    current.append(root)
    while current:
        next_level = []
        traversed = []
        for node in current:
            traversed.append(node.val)
            if node.left:
                next_level.append(node.left)  
            if node.right:
                next_level.append(node.right)  
        current = deque(next_level)
        res.append(traversed)
    return res
res = levelOrderPrint(root)
print(res[2])

