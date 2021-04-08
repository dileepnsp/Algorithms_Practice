class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    def addChild(self,child):
        child.parent=self
        self.children.append(child)
    def print_tree(self):
        print(self.get_level())
        spaces='   '*self.get_level()
        print(spaces+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

if __name__=="__main__":
    Doraswamy= TreeNode("Doraswamy")
    Dileep=TreeNode("Dileep")
    Praveen=TreeNode("Praveen")
    Renuka=TreeNode("Renuka")
    Doraswamy.addChild(Dileep)
    Doraswamy.addChild(Praveen)
    Doraswamy.addChild(Renuka)

    Dileep.addChild(TreeNode("Lekhana"))
    Dileep.addChild(TreeNode("Likith"))

    Praveen.addChild(TreeNode("Harsha"))
    Praveen.addChild(TreeNode("Damini"))

    Renuka.addChild(TreeNode("Devesh"))
    Renuka.addChild(TreeNode("Nithish"))

    Renuka.parent=Doraswamy
    Dileep.parent = Doraswamy
    Praveen.parent = Doraswamy

    Doraswamy.print_tree()
    #print(Renuka.children[0].get_level())





