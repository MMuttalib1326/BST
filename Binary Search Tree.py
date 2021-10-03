# Binary Search Tree
import QueueLinkedList1 as queue
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

# Level Order Traversal
def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
# Search 

def search(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data==nodeValue:
            print("The value is found")
        else:
            search(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild.data==nodeValue:
            print("The value is found")
        else:
            search(rootNode.rightChild,nodeValue)
     
# Delete
def minvalueNode(bstNode):
    current=bstNode
    while (current.leftChild is not None):
        current=current.leftChild
    return current
def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp 
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp 
        temp =minvalueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
        return rootNode

# Delete Entire Node
def deleteBST(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return"The BST has been succefully deleted"                   





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
#postorderTraversal(newBST)
#levelorderTraversal(newBST)
#search(newBST,10)
deleteNode(newBST,70)
deleteBST(newBST)
levelorderTraversal(newBST)

        