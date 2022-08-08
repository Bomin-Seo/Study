class TreeNode:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
    
class BST():
    def __init__(self):
        self.root = None
        self.order_list = []
    
    def is_empty(self):
        return self.root is None
    
    def count_nodes(self, tree):
        if tree is None:
            return 0
        else:
            return self.count_nodes(tree.left) + self.count_nodes(tree.right) + 1

    def length_is(self):
        return self.count_nodes(self.root)

    def insert(self, item):
        self.root = self.insert_item(self.root, item)

    def insert_item(self, node, item):
        tree = TreeNode(item)
        if node is None:
            node = tree
        elif item < node.info:
            node.left = self.insert_item(node.left, item)
        else:
            node.right = self.insert_item(node.right, item)
        return node

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.order_list.append(node.info)
            self.inorder(node.right)
    
    def preorder(self, node):
        if node is not None:
            self.order_list.append(node.info)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            self.order_list.append(node.info)

    def delete(self, item):
        self.delete_node(self.root, item)

    def delete_node(self, current, item):
        if current is not None:
            if item < current.info:
                current.left = self.delete_node(current.left, item)
            elif item > current.info:
                current.right = self.delete_node(current.right, item)
            else:
                if current.left is None:
                    current = current.right
                elif current.right is None:
                    current = current.left
                else:
                    tree = current.left
                    self.get_predecessor(tree, item)
                    current.info = item
                    del tree
            return current

    def get_predecessor(self, tree, data):
        while tree.right is not None:
            tree = tree.right
        data = tree.info
        return tree, data

