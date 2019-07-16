import random
import codecs
ct=0
split=[]
trainSet = set()
testSet = set()
for i in range(2268440):
    split.append(1)
for i in range(567110):
    split.append(0)

random.shuffle(split)
train_file='train_clks1.txt'
test_file='test_clks1.txt'
ct=0
with codecs.open('./uniqueUsers.txt','r','utf-8') as f:
    for line in f:
        if split[ct]==0:
            testSet.add(line.rstrip())
        else:
            trainSet.add(line.rstrip())
        ct+=1

ct=0
with codecs.open('./clks.dat','r','utf-8') as f:
    with codecs.open(test_file,'w','utf-8') as fw1:
        with codecs.open(train_file,'w','utf-8') as fw2:
            for line in f:
                if str(line.split()[0]) in testSet:
                    fw1.write(line)
                else:
                    fw2.write(line)
                ct+=1
