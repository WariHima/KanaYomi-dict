import csv
import re
#同じ単語があったら後の単語に単語コストを1追加する関数
#同じ単語で読みが英語の物があった場合削除

def cost_tyousei(merged_dict = list, load_dict = list):      
    i=0
    while merged_dict[i][0] in load_dict[:][0] and not i == len(merged_dict):
        v = i
        if not re.search('[ぁ-んァ-ヴ]*', load_dict[i][11]):
            print("削除行")
            print(load_dict[v])
            load_dict.pop(v)

        while not v == len(load_dict):
            if merged_dict[i][0] == load_dict[v][0]:
                cost = int(load_dict[v][3])
                cost += 1
                load_dict[v][3] = cost
                print("コスト変更")
                print(load_dict[v])

            v += 1
            
        i += 1
    return(load_dict)

out = "kanayomi-dict.csv"

files = [
    "neologd-ipa.csv",
    "atok11na.csv",
    "sangokushi.csv",
    "mjdicmsi.csv",
    "kana-unidic-csj.csv",
    "kana-naist-jdic.csv",
    "hiragana-unidic-csj.csv",
    "hiragana-naist-jdic.csv",
]

base = ["unidic-csj.csv","naist-jdic.csv"]

for i in base:
    with open(i, encoding='utf8') as f:
        csvreader = csv.reader(f)
        base_dict = [row for row in csvreader] 


i = 0
merged_dict = []

while not i == len(files):

    with open(str(files[i]), encoding='utf8') as f:
        csvreader = csv.reader(f)
        load_dict = [row for row in csvreader] 

    #ベースの辞書を代入
    if i == 0:
        merged_dict = load_dict
        i += 1
        print(i)
    else:
        merged_dict = merged_dict + cost_tyousei(base_dict,load_dict)
        i += 1
        print(i)

with open(out, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(merged_dict)