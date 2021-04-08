# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1=[5,4,3]
list2=[8,6,4]
prev=None
head1=None
head2=None
for i in list1:
    node = ListNode()
    node.val=i
    if prev is not None:
        prev.next=node
        prev=node
    else:
        prev=node
        head1=node
prev=None
for i in list2:
    node = ListNode()
    node.val=i
    if prev is not None:
        prev.next=node
        prev=node
    else:
        prev=node
        head2=node
tmp=head1
while tmp is not None:
    #print(tmp.val)
    tmp=tmp.next
tmp=head2
while tmp is not None:
    #print(tmp.val)
    tmp=tmp.next


def addTwoNumbers(l1: ListNode, l2: ListNode):
    head1=l1
    head2=l2
    total=""
    sum=0
    carry=0
    list1 = [5, 4, 3]
    list2 = [8, 6, 4]
    while  head1 is not None and head2 is not None:
        sum=head1.val+head2.val+carry
        print("sum:",sum)
        carry = sum // 10
        sum=sum%10
        print("prev total:",total)
        print("carry:",carry)
        print("sum:" ,sum)
        total=total+str(sum)
        head1=head1.next
        head2=head2.next
        print(total)
    print("final:"+total)
    print("reverse:",total[::-1])
addTwoNumbers(head1,head2)