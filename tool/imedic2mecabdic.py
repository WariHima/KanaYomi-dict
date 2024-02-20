import re 
import csv
import jaconv

filename = 'output.txt'
out_file = "out.csv"
result = []

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f, delimiter='\t')
    content = [row for row in csvreader] 
print(content)

for i in range(len(content)): 
    if len(content[i]) > 1:
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

with open(out_file, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(result)
