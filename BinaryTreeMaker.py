class Node:
    def __init__(self, val, left = None, right= None):
        self.val = val
        self.left =left
        self.right = right

class TreeMaker:
    def levelOrderBuilder(self,arr, root, root_pos, arr_len):
        if root_pos < arr_len:
            root = Node(arr[root_pos])
            root.left = self.levelOrderBuilder(arr, root.left, 2 * root_pos + 1, arr_len)
            root.right = self.levelOrderBuilder(arr, root.right, 2 * root_pos + 2, arr_len)
            return root 


