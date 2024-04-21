class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# initializing linked list
a.next=b
b.next=c
c.next=d

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
    current = head
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        print('prev--',prev.value)
        current = next
    return prev

def recReverseList(head,prev=None):
    if head == None: return
    print('item - ',prev,end='')
    next = head.next
    head.next = prev
    return recReverseList(next,head)

# reverse = recReverseList(a)
# printNodes(reverse) /
# aa = recReverseList(a)
print('linked-list = ',a.value)

def maxNode(head,counter=0):
    if head == None:return counter
    return maxNode(head.next,counter+1)
print('total-nodes = ',maxNode(a))
def zipLists(head1,head2):
    tail = None
    count = 0
    while head1 != None and head2 != None:
        if count % 2 == 0 :
            tail = head1
        else:
            tail.next = head2
    #find who have more nodes
    # start1 = max(maxNode(head1),maxNode(head2))
    #if head1 is greater than head 2 , loop should use head1 other than it should use head2
    #on the iteraction make this replacement
    """
    current = head
    next = current.next
    toAdd = head2
    current.next = toAdd
    nextToAdd = toAdd.next
    toAdd.next = next
    toAdd = nextToAdd
    """