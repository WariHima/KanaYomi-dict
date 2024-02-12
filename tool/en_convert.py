
# Licence GPLv2

import re 
import csv
import data

filename = ['naist-jdic.csv','unidic-csj.csv']

kanadict = []
result = []

yomi_dict = list(data.data.items())

with open(filename[0], encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 

with open(filename[1], encoding='utf8') as f:
    csvreader = csv.reader(f)
    content += [row for row in csvreader] 

#カタカナ語辞書作成
for i in range(len(content)): 
    if re.fullmatch('[ァ-ヴー]*', content[i][0]):
        kanadict.append(content[i])
#カタカナ語辞書と英語辞書を合体

for i in range(len(yomi_dict)): 

    dummylist = ["","",1,"*","*","*","*","*",]
    yomi = yomi_dict[i][1]
    word = yomi_dict[i][0]
    wordtype = "未選別"
    dummylist.insert(0,word)
    dummylist.insert(4,wordtype)
    dummylist.insert(10,word)
    dummylist.insert(11,yomi)
    dummylist.insert(12,yomi)

    mora = len(yomi_dict[i][1])
    dummydata = "0/" + str(mora)
    dummylist.append(dummydata)
    dummylist.append("*")
    result.append(dummylist)

#print(result)
yomilist = []
for i in range(len(kanadict)):
    yomilist.append(kanadict[i][0])


for i in range(len(result)):
    #print(i)
    if result[i][11] in yomilist:

        v = yomilist.index(result[i][11])
        kanadict[v][0] = result[i][0]
        print(kanadict[v])
        result[i] = kanadict[v]
        print(result[i])

with open('out.csv', 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator="\n")
    writer.writerows(result)