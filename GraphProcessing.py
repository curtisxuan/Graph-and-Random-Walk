import pickle
import codecs

def processList(G, out_file, length):
    ct=0
    out_file='graph2.txt'
    while ct<length:
        tempDict={}
        for i in G[0]:
            if i not in tempDict:
                tempDict[i]=1
            else:
                tempDict[i]+=1
        G.pop(0)
        with codecs.open(out_file,'a','utf-8') as f:
            for i in tempDict:
                if tempDict[i]!=1:
                    f.write(str(i) + ' ' + str(tempDict[i]) + '\t')
        #         G[ct].append((i,tempDict[i]))
            f.write('\n')
            f.close()
        ct+=1
#         if ct%10000==0:
#             print(ct)
#             print(len(b))
    return

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


def main():
    with open("./graph.txt", "rb") as fp:   # Unpickling
        G = pickle.load(fp)
    processList(G, 'graph1.txt', 2784203)
    ids,docids,offset,neighbors,weight = getMultipleLists('./graph1.txt','./uniqueIDs.txt')

    with open('model_file1.txt','w') as fw:
    for i in docids:
        fw.write(str(i) + '\t')
    fw.write('\n')
    for i in ids:
        fw.write(str(i) + '\t')
    fw.write('\n')
    for i in offset:
        fw.write(str(i) + '\t')
    fw.write('\n')
    for i in neighbors:
        fw.write(str(i) + '\t')
    fw.write('\n')
    for i in weight:
        fw.write(str(i) + '\t')
