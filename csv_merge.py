import csv

out = "kanayomi-dict.csv"
files = [
    "kana-unidic-csj.csv",
    "kana-naist-jdic.csv",
    "en-kana-unidic-csj.csv",
    "en-kana-naist-jdic.csv",
]

i = 0
merged_dict = []

while not i == len(files):
    with open(str(files[i]), encoding='utf8') as f:
        csvreader = csv.reader(f)
        load_dict = [row for row in csvreader] 
    merged_dict = merged_dict + load_dict
    i += 1
    print(i)

with open(out, 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator='\n')
    writer.writerows(merged_dict)