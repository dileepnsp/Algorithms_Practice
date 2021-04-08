class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    stack=Stack()
    print(stack.isEmpty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    #print(stack)
    print(stack.pop())
    #print(stack)
    print(stack.peek())
    print(stack.size())
    print(stack.items)
