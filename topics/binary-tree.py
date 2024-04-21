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