import re 
import csv
import jaconv

filename = 'atok11na.csv'

result = []

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 


i = 0
while not i == len(content): 

    dummylist = ["","",1,"*","*","*","*","*",]
    yomi = jaconv.hira2kata(content[i][0])
    word = content[i][1]
    wordtype = content[i][2]
    dummylist.insert(0,word)
    dummylist.insert(4,wordtype)
    dummylist.insert(10,word)
    dummylist.insert(11,yomi)
    dummylist.insert(12,yomi)
    result.append(dummylist)

    i += 1

with open(filename, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(result)
