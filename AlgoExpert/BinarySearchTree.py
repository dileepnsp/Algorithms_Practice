class BinarySearchTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addChild(self,data):
        if data==self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BinarySearchTree(data)
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()
        #print(self.data)
    def search(self,data):
        print(self.data)
        if self.data==data:
            print("Match")
            return True
        if data < self.data:
            if self.left:
                self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                self.right.search(data)
            else:
                return False

def build_binarysearchtree(lst):
        root=BinarySearchTree(lst[0])
        for i in range(1,len(lst)):
            root.addChild(lst[i])
        return root
if __name__=="__main__":
    lst=[17, 4, 1, 20, 9, 23, 18, 34]
    root=build_binarysearchtree(lst)
    #root.inorder_traversal()
    #print(root.search(20))
    print(root.search(20))





