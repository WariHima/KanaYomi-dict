
# Licence GPLv2

import re 
import csv
import data

filename = 'naist-jdic.csv'

kanadict = []
result = []

yomi_dict = list(data.data.items())

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 

print(yomi_dict)

#カタカナ語辞書作成
i = 0
while not i == len(content): 
    if re.fullmatch('[ァ-ヴー]*', content[i][0]):
        kanadict.append(content[i])
    i += 1

i = 0

#英語カタカナ読み辞書作成

i=0
while not i == len(kanadict):
    v=0

    while not v == len(yomi_dict): 
        if kanadict[i][0] == str(yomi_dict[v][1]):
            kanadict[i][0] = yomi_dict[v][0]
            result.append(kanadict[i])
            print(kanadict[i])
        v += 1
        
    print(str(i) + "行")
    i += 1

print(result)

with open('out.csv', 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator="\n")
    writer.writerows(result)