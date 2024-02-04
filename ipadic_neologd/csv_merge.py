import csv

out = "neologd-ipa.csv"
files = [
    "neologd-adjective-exp-dict-seed.20151126.csv",
    "neologd-adjective-std-dict-seed.20151126.csv",
    "neologd-adjective-verb-dict-seed.20160324.csv",
    "neologd-adverb-dict-seed.20150623.csv",
    "neologd-common-noun-ortho-variant-dict-seed.20170228.csv",
    "neologd-date-time-infreq-dict-seed.20190415.csv",
    "neologd-ill-formed-words-dict-seed.20170127.csv",
    "neologd-interjection-dict-seed.20170216.csv",
    "neologd-noun-sahen-conn-ortho-variant-dict-seed.20160323.csv",
    "neologd-proper-noun-ortho-variant-dict-seed.20161110.csv",
    "neologd-quantity-infreq-dict-seed.20190415.csv"
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