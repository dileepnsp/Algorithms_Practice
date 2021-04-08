import sys
class BTree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def add_child(self,data):
        if self.data==data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BTree(data)
    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print(self.data)
        if self.right:
            self.right.inorder_print()
    def pre_order_print(self):
        print(self.data)
        if self.left:
            self.left.inorder_print()
        if self.right:
            self.right.inorder_print()
    def post_order_print(self):
        if self.left:
            self.left.inorder_print()
        if self.right:
            self.right.inorder_print()
        print(self.data)
    def mirror_image(self):
        if self is None:
            return
        temp=self
        if self.left is not None:
            self.left.mirror_image()
        if self.right is not None:
            self.right.mirror_image()
        temp=self.left
        self.left=self.right
        self.right=temp

    def search_element(self,num):
        #print(self.data)
        if self.data==num:
            print("Yes Found")
            sys.exit()
        if num < self.data:
            if self.left:
                self.left.search_element(num)
            else:
                print("Not found")
        else:
            if self.right:
                self.right.search_element(num)
            else:
                print("Not found")

def Build_Btree(lst):
    root=BTree(lst[0])
    for i in lst[1:]:
        #print(i)
        root.add_child(i)
    return root
if __name__ == "__main__":
    #print("In main..")
    lst=[3,1,5,9,2,4]
    root=Build_Btree(lst)
    #print("In order")
    root.inorder_print()
    #print("Preorder")
    #root.pre_order_print()
    #print("Postorder")
    #root.post_order_print()
    #root.search_element(40)
    root.mirror_image()
    root.inorder_print()