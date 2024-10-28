class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree():
    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(40)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)
    return root

#Task 1
def in_order_traversal(node, result):
    if node:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)

def in_order(tree):
    result = []
    in_order_traversal(tree, result)
    return result

#Task 2
def pre_order_traversal(node, result):
    if node:
        result.append(node.value)
        pre_order_traversal(node.left, result)
        pre_order_traversal(node.right, result)

def pre_order(tree):
    result = []
    pre_order_traversal(tree, result)
    return result

#Task 3
def post_order_traversal(node, result):
    if node:
        post_order_traversal(node.left, result)
        post_order_traversal(node.right, result)
        result.append(node.value)

def post_order(tree):
    result = []
    post_order_traversal(tree, result)
    return result

#Task 4
def test_traversals():
    tree = build_tree()
    
    in_order_result = in_order(tree)
    pre_order_result = pre_order(tree)
    post_order_result = post_order(tree)
    
    print("In-Order Traversal:", in_order_result)
    print("Pre-Order Traversal:", pre_order_result)
    print("Post-Order Traversal:", post_order_result)

# Run the test
test_traversals()
