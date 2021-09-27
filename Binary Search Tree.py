# Binary Search Tree
class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
# Insertion

def insertNode(rootNode,nodeValue):
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)   
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)
    return "The node has been succefully inserted"

# Preorder Traversal

def preorderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild) 

# InorderTraversal

def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightChild)

# Post Order Traversal
def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftChild)
    postorderTraversal(rootNode.rightChild)
    print(rootNode.data)        


newBST=BSTNode(None)
#print(insertNode(newBST,70))                             
#print(insertNode(newBST,60))
insertNode(newBST,70)
insertNode(newBST,80)
insertNode(newBST,90)
insertNode(newBST,100)
insertNode(newBST,110)
insertNode(newBST,50)
insertNode(newBST,40)
#print(newBST.data)
#print(newBST.leftChild.data) 
#preorderTraversal(newBST)
#inorderTraversal(newBST)
postorderTraversal(newBST)

        