class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_recursive(node.right, temp.value)
        return node

    def height(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))

    def level_max(self):
        temp = []
        temp.append(self.root)
        res = []
        while len(temp) > 0:
            maxi = 0
            for i in range(len(temp)):
                if temp[0].left is not None:
                    temp.append(temp[0].left)
                if temp[0].right is not None:
                    temp.append(temp[0].right)
                maxi = max(temp[0].value, maxi)
                temp.pop(0)
            res.append(maxi)
        print(res)

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def min(self):
        current = self.root
        while current.right:
            current = current.right
        print(current.value)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=" ")

bst = BinarySearchTree()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Level Max")
    print("8. Min")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to insert: "))
        bst.insert(value)
    elif choice == 2:
        value = int(input("Enter the value to delete: "))
        bst.delete(value)
    elif choice == 3:
        value = int(input("Enter the value to search: "))
        result = bst.search(value)
        if result:
            print("Value found:", result.value)
        else:
            print("Value not found")
    elif choice == 4:
        print("Inorder Traversal:", end=" ")
        bst.inorder_traversal(bst.root)
        print()
    elif choice == 5:
        print("Preorder Traversal:", end=" ")
        bst.preorder_traversal(bst.root)
        print()
    elif choice == 6:
        print("Postorder Traversal:", end=" ")
        bst.postorder_traversal(bst.root)
        print()
    elif choice == 7:
        bst.level_max()
    elif choice == 8:
        bst.min()
    elif choice == 9:
        break
    else:
        print()