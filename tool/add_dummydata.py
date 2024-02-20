
import csv

filename = 'atok11na.csv'

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    in_dict = [row for row in csvreader] 

i = 0
#add dummydata
for i in range(len(in_dict)): 

    mora = len(in_dict[i][11])
    dummydata = "0/" + str(mora)
    in_dict[i].append(dummydata)
    in_dict[i].append("*")

with open(filename, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(in_dict)