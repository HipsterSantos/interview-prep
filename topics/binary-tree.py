import sys


class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

def depthFirstSearch(root):
    if root is None: return []
    stack = [root]
    result = []
    while(len(stack)>0):
        current_node = stack.pop()
        print('pick current element , if have more add to traverse ',current_node.value)
        result.append(current_node.value)
        if current_node.right: stack.append(current_node.right)
        if current_node.left: stack.append(current_node.left)


depthFirstSearch(a)

def recDepthFirst(root):
    if root is None: return []
    lefts = recDepthFirst(root.left)
    rights = recDepthFirst(root.right)
    return [root.value, *lefts, *rights ]

print('result = ',recDepthFirst(a))

print('pop--',[3,2,3,4].pop(1))

def breadthFirst(root):
    if root is None: return []
    queue = [root]
    result = []
    while len(queue)>0:
        current_node = queue.pop(0)
        result.append(current_node.value)
        if current_node.left: queue.append(current_node.left)
        if current_node.right: queue.append(current_node.right)
    return result
print('BreadthFirst = ',breadthFirst(a))

def treeInclude(root,e):
    stack = [root]
    while len(stack)>0:
        current_node = stack.pop()
        if current_node.value == e: return True
        if current_node.left: stack.append(current_node.left)
        if current_node.right: stack.append(current_node.right)
    return False

print('\nincludes- C- ',treeInclude(a,'G'))


def recDepthFirstInclude(root,target):
    if root is None: return False
    if root.value == target: return True
    return recDepthFirstInclude(root.left,target) or recDepthFirstInclude(root.right, target)

print('recDepthFirstInclude2 = ',recDepthFirstInclude(a,'G'))

def reDepthFirstSum(root):
    if root is None: return 0
    return root.value + reDepthFirstSum(root.left) + reDepthFirstSum(root.right)

#iteractively solution
def depthFirstSum(root):
    if not root: return 0
    queue = [root]
    totalSum = 0
    while len(queue)>0:
        current_node = queue.pop(0)
        totalSum += current_node.value
        if current_node.left: queue.append(current_node.left)
        if current_node.right: queue.append(current_node.right)
    return totalSum

def depthFirstMinimum(root):
    if not root: return int(sys.maxsize)
    return min(root.value, min(depthFirstMinimum(root.left),depthFirstMinimum(root.right)))

one = TreeNode(33)
two = TreeNode(7)
three = TreeNode(6)
four =  TreeNode(344)
five =  TreeNode(8)

one.left = two
one.right = three
two.left = four
two.right = five

print('minimum  = ',depthFirstMinimum(one))

def depthFirstItMinimum(root):
    if not root: return 0
    queue = [root]
    minimum = float('inf')
    while len(queue) >0:
        current_node = queue.pop(0)
        if current_node.value < minimum:
            minimum = current_node.value
        if current_node.left: queue.append(current_node.left)
        if current_node.right: queue.append(current_node.right)
    return minimum

print('it-minimum = ',depthFirstItMinimum(one))