import csv
import re
import jaconv

filename = 'naist-jdic.csv'

result = []

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 

#平仮名のみの単語を削除
i = 0
while not i == len(content):
    if re.fullmatch('[ぁ-んー]*', content[i][0]):
        print(str(i) + "行を削除")
        content.pop(i)
    i += 1

i = 0
while not i == len(content): 
    content[i][0] = content[i][11]
    content[i][0] = jaconv.kata2hira(content[i][0])
    result.append(content[i])
    i += 1

#print(result)

with open("kana-" + filename, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(result)