import codecs
import random

def getMultipleLists(graph_file,ids_file):
    offset=[]
    offsetCt=0
    neighbors=[]
    weight=[]
    ids=set()
    ct=0
    with codecs.open(graph_file,'r','utf-8') as f:
        for line in f:
            articles=line.rstrip().split('\t')
            if articles[0]=='':
                ct+=1
                continue
            ids.add(ct)
            offset.append(offsetCt)
            offsetCt+=len(articles)
            for article in articles:
                neighbors.append(article.split(' ')[0])
            for article in articles:
                weight.append(article.split(' ')[1])
    #         if ct==5:
    #             break
            ct+=1
    docids=[]
    ct=0
    with codecs.open(ids_file,'r','utf-8') as f:
        for line in f:
            if ct in ids:
                docids.append(line.rstrip())
            ct+=1
    # print(len(ids))
    # print(len(docids))
    # print(len(offset))
    # print(len(neighbors))
    # print(len(weight))
    return [ids,docids,offset,neighbors,weight]

# generate new node and change currNode
def generateRandomNode(currNode,offset,neighbors,weight,mapping):
    # get count of neighbors
    neighborCount=0
    if currNode==len(offset)-1:
        neighborCount=len(neighbors)-offset[currNode]
    else:
        neighborCount=int(offset[currNode+1])-int(offset[currNode])
    
    weightTotal=0
    for i in range(neighborCount):
        weightTotal += int(weight[offset[currNode]+i])
    
    randNum = random.randint(0,weightTotal)
    
    ct=0
    for i in range(neighborCount):
        randNum -= int(weight[offset[currNode]+i])
        if randNum<=0:
            break
        ct+=1
    currNode = mapping[neighbors[offset[currNode]+ct]]
    return currNode
    
# return dict of visited nodes
def randomWalk(Node,N,walkLen,offset,neighbors,weight,mapping):
    totSteps=0
    V={}
    while totSteps < N:
        currNode = Node
        for i in range(walkLen):
#             generateRandomNodesInWalk and update currPin
            currNode = generateRandomNode(currNode,offset,neighbors,weight,mapping)
            if currNode in V:   
                V[currNode]+=1
            else:
                V[currNode]=1
        totSteps += walkLen
    return V


ids,docids,offset,neighbors,weight = getMultipleLists('./graph1.txt','./uniqueIDs.txt')

s = sorted(ids,key=int)
mapping={}
ct=0
for i in s:
    mapping[str(i)]=ct
    ct+=1

# randomWalk(Node,N,walkLen,offset,neighbors,weight,mapping)
test = randomWalk(0,10,3,offset,neighbors,weight,mapping)
print(test)

# print(docids[0])
# print(docids[415662])

