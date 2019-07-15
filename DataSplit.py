import random
import codecs
ct=0
split=[]
for i in range(100589284):
    split.append(1)
for i in range(25147321):
    split.append(0)
print(len(split))
random.shuffle(split)
# train=[]
# test=[]
train_file='train_clks.txt'
test_file='test_clks.txt'
ct=0

with codecs.open('./clks.dat','r','utf-8') as f:
    with codecs.open(test_file,'w','utf-8') as fw1:
        with codecs.open(train_file,'w','utf-8') as fw2:
            for line in f:
                if split[ct]==0:
                    fw1.write(line)
                else:
                    fw2.write(line)
                ct+=1
print(ct)