from BinarySearchTrees import TreeNode

class BinsTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        newnode = TreeNode.TreeNode(data)

        if self.root is None:
            self.root = newnode
            return self.root
        else:
            p = self.root
            while True:
                if p.data > newnode.data:
                    if p.left is None:
                        p.left = newnode
                        return p.left
                    else:
                        p = p.left
                elif p.data < newnode.data:
                    if p.right is None:
                        p.right = newnode
                        return p.right
                    else:
                        p = p.right
                else:
                    return p

    def search(self, data):
        if self.root.data == data:
            return self.root, None

        p = self.root

        while p is not None:
            if p.data > data:
                parent = p
                p = p.left
            elif p.data < data:
                parent = p
                p = p.right
            else:
                return p, parent

        return None, None

    def remove(self, data):
        rem, parent = self.search(data)

        if rem is None:
            return None

        if parent is None:
            self.root = rem.left
            p = self.root

        else:
            if rem == parent.left:
                parent.left = rem.left
                p = parent.left

            elif rem == parent.right:
                parent.right = rem.right
                p = parent.right

        if p is not None:
            while p.right is not None:
                p = p.right

            p.right = rem.right

        return rem

    def printBF(self):
        queue = []

        queue.append(self.root)

        while len(queue) > 0:
            cur = queue.pop(0)
            print(cur.data, end=" ")
            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)

        print()

    def printIOrec(self, node):
        if node is not None:
            self.printIOrec(node.left)
            print(node.data, end=" ")
            self.printIOrec(node.right)

    def printInOrder(self):
        self.printIOrec(self.root)
        print()

    def printPOrec(self, node):
            if node is not None:
                print(node.data, end=" ")
                self.printPOrec(node.left)
                self.printPOrec(node.right)

    def printPreOrder(self):
        self.printPOrec(self.root)
        print()

    def printSOrec(self, node):
        if node is not None:
            self.printSOrec(node.left)
            self.printSOrec(node.right)
            print(node.data, end=" ")

    def printPostOrder(self):
        self.printSOrec(self.root)
        print()






