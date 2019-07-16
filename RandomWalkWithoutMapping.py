import codecs
import random

# generate new node and change currNode
def generateRandomNode(currNode,offset,neighbors,weight):
    # get count of neighbors
    neighborCount=0
    if currNode==len(offset)-1:
        neighborCount=len(neighbors)-offset[currNode]
    else:
        neighborCount=int(offset[currNode+1])-int(offset[currNode])
    
    weightTotal=0
    for i in range(neighborCount):
        weightTotal += int(weight[int(offset[currNode])+i])
    
    randNum = random.randint(0,weightTotal)
    
    ct=0
    for i in range(neighborCount):
        randNum -= int(weight[int(offset[currNode])+i])
        if randNum<=0:
            break
        ct+=1
    currNode = neighbors[int(offset[currNode])+ct]
    return int(currNode)
    
# return dict of visited nodes
def randomWalk(Node,N,walkLen,offset,neighbors,weight):
    totSteps=0
    V={}
    while totSteps < N:
        currNode = Node
        for i in range(walkLen):
#             generateRandomNodesInWalk and update currPin
            currNode = generateRandomNode(currNode,offset,neighbors,weight)
            if currNode in V:   
                V[currNode]+=1
            else:
                V[currNode]=1
        totSteps += walkLen
    return V

def readTwoColFile(in_file):
    L1=[]
    L2=[]
    with codecs.open(in_file,'r','utf-8') as f:
        for line in f:
            e1,e2 = line.rstrip().split()
            L1.append(e1)
            L2.append(e2)
    return [L1,L2]

# Read in Graph
in_file1 = './doc-offset.txt'
in_file2 = './neighbor-weight.txt'
docids,offset = readTwoColFile(in_file1)
neighbors,weight = readTwoColFile(in_file2)

# Run Walk Algorithm
# randomWalk(Node,N,walkLen,offset,neighbors,weight)
test = randomWalk(0,30,5,offset,neighbors,weight)
print(test)


