# import networks as nx
# import matplotlbi.pyplot as plt
import codecs
#sort list in ascending order based on 3rd index
def Sort(sub_li):
    sub_li.sort(key = lambda x: x[2]) 
    return sub_li 

#create mapping dictionary of article IDs and indices
def createDic(in_file):
    result={}
    ct=0
    with codecs.open(in_file,'r','utf-8') as f:
        for line in f:
            result[line.rstrip()]=ct
            ct+=1
    return result

#create array of article IDs
def getArray(in_file):
    result={}
    with codecs.open(in_file,'r','utf-8') as f:
        for line in f:
            result.append(line.rstrip())
    return result


def processDoc(G,in_file,firstUser,articleDict):
    ct=0
    prevUser=firstUser
    userList=[]
    nodeList=[]
    with codecs.open(in_file, 'r', 'utf-8') as f:
        for line in f:
            info = line.split()
            if info[0]==prevUser:    # same user, append to list
                userList.append(info)
            else:    #diff user, add connections and update for new user
                Sort(userList)
                prevTime=int(userList[0][2])
                for i in userList:
                    if int(i[2]) - prevTime <1800: # if within 30 min gap
                        nodeList.append(articleDict[i[1]])
                        prevTime = int(i[2])
                    else:    # else diff session
                        addNodes(G,nodeList)
                        nodeList=[articleDict[i[1]]]
                        prevTime = int(i[2])
                addNodes(G,nodeList)

                nodeList=[]
                userList = [info]
                prevUser = info[0]            
#             print(info)
            if ct%1000000==0:
                print(ct)
#             if ct==10:
#                 break
            ct+=1

    #get the last user case (same code as the else section)
    Sort(userList)
    prevTime=int(userList[0][2])
    for i in userList:
        if int(i[2]) - prevTime <1800: # if within 30 min gap
            nodeList.append(articleDict[i[1]])
            prevTime = int(i[2])
        else:    # else diff session
            addNodes(G,nodeList)
            nodeList=[articleDict[i[1]]]
            prevTime = int(i[2])
    addNodes(G,nodeList)

# # Array Dictionary Representation
# def addNodes(G,L):
#     for i in range(len(L)): # for all nodes
#         for j in range(i+1,len(L)):
#             if L[j] not in G[L[i]]:
#                 G[L[i]][L[j]]=1
#                 G[L[j]][L[i]]=1
#             else:
#                 G[L[i]][L[j]]+=1
#                 G[L[j]][L[i]]+=1
    
# # Array pair representation
# def addNodes(G,L):
#     for i in range(len(L)): # for all nodes
#         for j in range(i+1,len(L)):
#             isIn = False
#             ct=0
#             for k in G[L[i]]:
#                 if L[j]==k[0]:
#                     isIn=True
#                     break
#                 ct+=1
#             if isIn: #if node already exists
#                 G[L[i]][ct][1]+=1
#                 for x in G[L[j]]:
#                     if x[0]==L[i]:
#                         x[1]+=1
#             else:
#                 G[L[i]].append([L[j],1])
#                 G[L[j]].append([L[i],1])

# # Array representation
def addNodes(G,L):
    for i in range(len(L)): # for all nodes
        for j in range(i+1,len(L)):
            G[L[i]].append(L[j])
            G[L[j]].append(L[i])


# # Graph representation
# def addNodes(G,L):
#     for i in range(len(L)): # for all nodes
#         if L[i] in G.nodes(): #if node already exists, connect the existing node to the rest
#             for j in range(i+1, len(L)):
#                 if L[j] in G.nodes():
#                     G.add_edge(L[i],L[j])
#                 else:
#                     G.add_node(L[j])
#                     G.add_edge(L[i],L[j])
#         else: #else, create node and connect to the rest
#             G.add_node(L[i])
#             for j in range(i+1, len(L)):
#                 if L[j] in G.nodes():
#                     G.add_edge(L[i],L[j])
#                 else:
#                     G.add_node(L[j])
#                     G.add_edge(L[i],L[j])
#     return G

# #   graph representation
#     G=nx.Graph()

# #   list of dict representation
#     G = [{} for x in range(2784203)]

#   list of list representation
G = [[] for x in range(2784203)]

in_file='./uniqueIDs.txt'
articleDict=createDic(in_file)
    
in_file = './train_clks1.txt'
processDoc(G,in_file,'10000225', articleDict)

import pickle
with open("graph.txt", "wb") as fp:   #Pickling
    pickle.dump(G, fp)
