import csv
import re
#同じ単語があったら後の単語に単語コストを1追加する関数
#同じ単語で読みが英語の物があった場合削除

def cost_tyousei(merged_dict = list, load_dict = list):    

    for i in range(len(merged_dict)):
        mergeddic_words = merged_dict[i][0]

    for i in range(len(load_dict)):
        if not re.search('[ぁ-んァ-ヴ]*', load_dict[i][11]):
            print("削除行")
            print(load_dict[i])
            load_dict.pop(i)

    for i in range(len(load_dict)):
    
        if load_dict[i][0] in mergeddic_words:
            print(i)
        
            for v in range(len(merged_dict)):

                if merged_dict[v][0] == load_dict[i][0]:
                    cost = int(load_dict[i][3])
                    cost += 1
                    load_dict[i][3] = cost
                    print("コスト変更")
                    print(load_dict[i])

                     
    return(load_dict)

out = "kana-yomi-dict.csv"

files = [
    "neologd-ipa.csv",
    "katakana-dict.csv",
    "hiragana-dict.csv",
    "emoji-yomi.csv",
    "atok11na.csv",
    "sangokushi.csv",
    "mjdicmsi.csv",
]

base = ["unidic-csj.csv","naist-jdic.csv"]

for i in base:
    with open(i, encoding='utf8') as f:
        csvreader = csv.reader(f)
        base_dict = [row for row in csvreader] 


i = 0
merged_dict = []

for i in range(len(files)):

    with open(str(files[i]), encoding='utf8') as f:
        csvreader = csv.reader(f)
        load_dict = [row for row in csvreader] 
    #一番目の辞書を代入
    if i == 0:
        merged_dict = load_dict
        print(i)
    else:
        merged_dict = merged_dict + cost_tyousei(base_dict,load_dict)
        print(i)

with open(out, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(merged_dict)