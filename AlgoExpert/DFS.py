class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, op):
        # Write your code here.
        if len(self.children) !=0:
            for child in self.children:
                op.append(child.name)
                child.depthFirstSearch(op)

if __name__=="__main__":
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    lst=[]
    lst.append(graph.name)
    graph.depthFirstSearch(lst)
    print(lst)
