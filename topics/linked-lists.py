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
        
def rec(head):
    if head is None: return 
    print(f"current Node = ",head)
    rec(head.next)