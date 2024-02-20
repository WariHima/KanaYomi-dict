import re
import csv

filename = "mjdicmsi.csv"
with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    load_dict = [row for row in csvreader] 


    

for i in range(len(load_dict)):
    #読みがカタカナ以外の物を削除。
    if not re.fullmatch('[ァ-ヴ]*', load_dict[i][11]):
        print("削除行")
        print(load_dict[i])
        load_dict.pop(i)
        v = i

    while not v == len(load_dict):
        if load_dict[i][0] == load_dict[v][0]:
            cost = int(load_dict[v][3])
            cost += 1
            load_dict[v][3] = cost
            print(load_dict[v][3])
            print(load_dict[v])

        v += 1

with open(filename, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(load_dict)
