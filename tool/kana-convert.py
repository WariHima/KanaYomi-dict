import csv
import jaconv

filename = 'unidic-csj.csv'

result = []

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 

i = 0
while not i == len(content): 
    content[i][0] = content[i][11]
    content[i][0] = jaconv.kata2hira(content[i][0])
    result.append(content[i])
    i += 1

print(result)

with open("kana-" + filename, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(result)