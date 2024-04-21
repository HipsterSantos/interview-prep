class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

def printNodes(head):
    current = head
    while head is not None: 
        print("value--",current.value)
        current = current.next
def sumNode(head):
    sum = 0
    while head != None:
        sum += sum + head.value
        head = head.next
    return sum
def findNode(head,index,value=None):
    counter = 0
    if head.value == value : return head
    while head != None:
        if counter == index: return head
        counter += 1
        head = head.next
def reverseList(head):
