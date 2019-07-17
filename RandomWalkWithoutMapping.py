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

import requests
from lxml.html import fromstring


docidSet = set(docids)
docToIndex={}
for i in range(len(docids)):
    docToIndex[docids[i]]=i
prevUser='10002933'
articles=[]
prevTime=0
accuracy=0
count=0
with codecs.open('train_clks1.txt','r','utf-8') as f:
    for line in f:
        if count==10:
            break
        user,article,time = line.rstrip().split()
#         print(prevTime-int(time))
#         prevTime=int(time)
        if user==prevUser:
            articles.append(article)
        else:
#             print(articles)
            if len(articles)<6:
                articles=[article]
                prevUser=user
            else:
                numArticles = len(articles)
                if numArticles>10:
                    numArticles=10
                iterAcc=0
                articleCount=0
                articles.reverse()
                #DO THE TEST HERE
                for i in range(3): #3 articles for predicting
                    predictions=[]
                    if articles[i] in docidSet: #article has to be in graph
                        articleCount+=1
#                         print(docToIndex[articles[i]])
                        resultDict = randomWalk(docToIndex[articles[i]],10,1,offset,neighbors,weight)
                        
                        result_sorted_keys = sorted(resultDict, key=resultDict.get)
                        # add top visited article to predictions
                        ct=0
                        for j in result_sorted_keys:
#                             print(j,resultDict[j])
                            if ct<numArticles:
                                if docids[j]==articles[i]:
                                    continue
                                predictions.append(docids[j])
                                ct+=1
                            else:
                                break
#                         print(articles)
#                         print(str(articleCount)+ ' ' + articles[i])
#                         r = requests.get('https://www.newsbreakapp.com/news/'+ articles[i])
#                         tree = fromstring(r.content)
#                         tree.findtext('.//title')
#                         print('\nORIGINAL: ' + str(tree.findtext('.//title')))
                        for index in range(ct):
#                             r = requests.get('https://www.newsbreakapp.com/news/'+ predictions[index])
#                             tree = fromstring(r.content)
#                             tree.findtext('.//title')
#                             print(tree.findtext('.//title'))
#                             print(predictions[index])
                            if predictions[index] in articles:
#                                 print(ct)
                                iterAcc+=1/ct
                                print('match')
                if articleCount==0:
                    articles=[article]
                    prevUser=user
                    continue
                
                accuracy+= iterAcc/articleCount
                count+=1
                articles=[article]
                prevUser=user
print(accuracy/count)
                
        

