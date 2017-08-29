class BinaryTree:
 
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder_iterative(self):
        pre_ordered_list = []
        stack = [self]
        while stack:
            node = stack.pop()
            if node:
                pre_ordered_list.append(node.get_root_val())
                stack.append(node.get_right_child())
                stack.append(node.get_left_child())
        return pre_ordered_list
    
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
