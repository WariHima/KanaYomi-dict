import re
import csv

filename = "atok11na.csv"
with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    load_dict = [row for row in csvreader] 

dellist = []

#複数読みがある名前を削除

i=-1 
while not i == len(load_dict):
    #読み方にカタカナ以外が含まれる単語を削除
    if not re.fullmatch('[ァ-ヴー]*', load_dict[i][11]):
        print("カタカナが以外が含まれる単語の行")
        print(load_dict[i])
        load_dict.pop(i)
    i += 1

i=-1        
v = i
while not i == len(load_dict):
    v = i
    v += 1

    #重複した言葉を削除
    while not v == len(load_dict):
        if load_dict[i][0] == load_dict[v][0]:

            load_dict.pop(v)
            print("削除行")
            print(load_dict[i])
            dellist.append(i)

        else:
            v += 1
    
    i += 1

print(dellist)
print(len(load_dict))

with open("out.csv", 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(load_dict)