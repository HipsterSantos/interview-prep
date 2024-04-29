"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


"""

class ListNode: 
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
def sumTwoLists(l1,l2):
    dumbList = ListNode(0)
    carry = 0
    current = dumbList
    while l1 or l2:
        val1 = l1.val if l1 else 0
        val2 = l2.val  if l2 else 0
        total = val1+val2+carry
        carry = total//10
        digit = total%10
        current.next = ListNode(digit)
        if l1 is not None: l1 = l1.next 
        if l2 is not None: l2 = l2.next
    return dumbList.next
        
        # class LinkedList(Node): 
#     head = None
#     size = 0
#     def __init__(self, head: Node = None):
#         if head != None:
#             self.head = head
#             self.size +=1
#     def insert(self,node):
#         if self.head is None: 
#             self.head = node
#         else:
#             temp = self.head 
#             self.head = node
#             self.head.next = temp
#         self.size +=1

#     def insert(self,value,index):
#         counter = 0
#         while counter <=index:
#             if counter == index: 

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         stack1,stack2 = [],[]
#         while l1 != None and l2 != None:
#             stack1.append(l1.val)
#             stack2.append(l2.val)
#             l1 = l1.next 
#             l2 = l2.next
#         #join all element of array 
#         #342
#         #465
#         stack1str = [str(c) for c in stack1]
#         stack2str = [str(b) for b in stack2]
#         delimiter = ""
#         str1 = int (delimiter.join(stack1str[::-1]))
#         str2 = int(delimiter.join(stack2str[::-1]))

#         print(f"stack1 {stack1str}  - stack2 {stack2str}")
#         print(f"stack1 {str1}  - stack2 {str2}")

#         summ = str1 + str2
#         reminder = summ % 10
#         newNode = ListNode(reminder)
#         while summ /10 != 0:
#             newNode.next(ListNode(reminder%10))
#         return newNode