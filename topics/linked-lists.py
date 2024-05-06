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
# Node (done) node->value, node->next
# linkedList
# linked list insertion  insert(a), insert(a,2)
#linked list delete  element in specific position delL(b)
# zip two linked list  zipL(head1,head2)
# swap positions swap(a,b)


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def insert(self,node:Node):
        if self.head is None:
            self.head = node
            self.size+=1
        else:
            self.head.next = node
            self.size+=1
    
    def isEmpty(self):
        return self.size == 0
    
    def insert(self,node:Node,index:int):
        if self.head is None:
            #first node is empty
            self.head = node
        else:
            #it means we already have a node
            temp = self.head
            self.head = node
            self.head.next = temp
        self.size+=1 #for every insertion operation we're couting
    def delete(self,item):
        current_node = self.head
        counter = 0
        while current_node != None:
            if current_node.value == item:
                if counter == 0:
                    self.head = current_node.next #if we're remove the first element , we can point th next to this first element
                else:
                    next = current_node.next
                    self.head.next = next
            counter +=1
            current_node = current_node.next
    def zipLists(self,head1,head2):
        pass
    @property
    def totalNodes(self):
        return self.size
    
    
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
def removeNthNode(head,n):
    dummy = ListNode(0,head)
    first,second = dummy,dummy
    #once we create a dummy , now dummy have the following [0]->[1]->[2]->[3]->[4]->5] 
    # original list = [1]->[2]->[3]->[4]->5]
    for _ in range(n+1):
        first = first.next # starts a 0 node till n+1 = n = 2 => 2+1 = 3 node [2]
    while first is not None:
        first = first.next
        second = second.next
    #next twice to skip the current element
    second.next = second.next.next
    return dummy.next