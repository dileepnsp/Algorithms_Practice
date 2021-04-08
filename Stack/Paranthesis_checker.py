from Algoritham_Practice.Stack.Stack_implement import Stack
def paranth_check(string,stack):
    size=len(string)
    i=0
    while i < size:
        if string[i] == ")" :
            if stack.size() != 0:
                stack.pop()
            else:
                print("Invalid")
                break;
        else:
            stack.push(string[i])
        i=i+1
    if stack.size() == 0:
        print("invalid")
    else:
        print("not valid")

if __name__ == '__main__':
    stack=Stack()
    paranth_check("((())))",stack)