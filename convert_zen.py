
# Licence GPLv2

import re 
import csv
import mojimoji

filename = 'en-kana-naist-jdic.csv'

with open(filename, encoding='utf8') as f:
    csvreader = csv.reader(f)
    content = [row for row in csvreader] 


#全角に変換
i = 0
  
while not i == len(content): 
    content[i][0] = mojimoji.han_to_zen(content[i][0])
    i += 1

with open(filename, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(content)