
class NodeType:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class IterBST():
    def __init__(self):
        self.root = None
        self.order_list = []

    def insert(self, data):
        node = NodeType(data)
        root = self.root
        if root is None:
            self.root = node
        else:
            node1 = self.find_node(root, data)
            node1.info = data

    def find(self, key):
        node = self.root
        while node:
            if node.info == key:
                return True
            elif node.info > key:
                node = node.left
            else:
                node = node.right
        return False

    def find_node(self, root, key):
        found = False
        temp_node = NodeType(0)
        while root is not None and not found:
            if key < root.info:
                if root.left is None:
                    root.left = temp_node
                    found = True
                root = root.left
            elif key > root.info:
                if root.right is None:
                    root.right = temp_node
                    found = True
                root = root.right
            else:
                found = True
        return root

    def delete(self, key):
        self.delete_node(self.root, key)

    def delete_node(self, node, key):
        found = False
        parentnode = None
        while node is not None and not found:
            if key < node.info:
                while key < node.info:
                    parentnode = node
                    node = node.left
            elif key > node.info:
                while key > node.info:
                    parentnode = node
                    node = node.right
            else:
                found = True
                if parentnode.left == node:
                    if node.left is None:
                        parentnode.left = node.right
                    elif node.right is None:
                        parentnode.left = node.left
                    else:
                        tree = node.left
                        self.get_predecessor(tree, key)
                        node.info = key
                        del tree
                elif parentnode.right == node:
                    if node.left is None:
                        parentnode.right = node.right
                    elif node.right is None:
                        parentnode.right = node.left
                    else:
                        tree = node.left
                        self.get_predecessor(tree, key)
                        node.info = key
                        del tree

# cpp대로 구현하셔야한다고 하셔서 재귀함수로 구현하였습니다.
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

    def get_predecessor(self, tree, data):
        while tree.right is not None:
            tree = tree.right
        data = tree.info
        return tree, data

