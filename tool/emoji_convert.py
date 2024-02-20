from pykakasi import kakasi,wakati
import mojimoji
import json 
import csv

with open('emoji_ja.json',encoding="utf8") as f:
    inputdict = json.load(f)

result = []
wordlist = list(inputdict)
print(wordlist)

kakasi = kakasi()
kakasi.setMode("J","K")
kakasi.setMode("H","K")
conv = kakasi.getConverter()

for i in range(len(inputdict)):
    emojilist = ["","",9999,"*","*","*","*","*",]
    word = wordlist[i]
    yomi = conv.do(inputdict[str(word)]["short_name"])
    yomi = mojimoji.han_to_zen(yomi)
    
    wordtype = "UNICODE記号・絵文字"
    emojilist.insert(0,word)
    emojilist.insert(4,wordtype)
    emojilist.insert(10,word)
    emojilist.insert(11,yomi)
    emojilist.insert(12,yomi)

    mora = len(yomi)
    dummydata = "0/" + str(mora)
    emojilist.append(dummydata)
    emojilist.append("*")
    result.append(emojilist)

with open('out.csv', 'w', encoding='utf8',) as f:
    writer = csv.writer(f,lineterminator="\n")
    writer.writerows(result)