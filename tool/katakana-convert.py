import csv
import re
import jaconv

result = []

with open('naist-jdic.csv', encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 

with open('unidic-csj.csv', encoding='utf8') as f:
    csvreader = csv.reader(f)
    content += [row for row in csvreader] 
    
#カタカナのみの単語を削除
i = 0
while not i == len(content):
    if re.fullmatch('[[ァ-ヴー]]*', content[i][0]):
        print(str(i) + "行を削除")
        content.pop(i)
    i += 1

i = 0
while not i == len(content): 
    content[i][0] = content[i][11]
    result.append(content[i])
    i += 1

#print(result)

with open("katakana-dict.csv", 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(result)