import re 
import csv
import jaconv

filename = 'naist-jdic.csv'

result = []

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 

i = 0
while not i == len(content): 
    if re.fullmatch('[ァ-ヴー]*', content[i][0]):
        content[i][0] = jaconv.kata2hira(content[i][0])
        result.append(content[i])
    i += 1

print(result)

with open('out.csv', 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(result)