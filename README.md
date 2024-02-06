# KanaYomi-dict openjtalk形式の多言語カタカナ読み辞書 
openjtalk系の辞書の登録語句を増やし解析できない単語を減らす目的で作成しました。  

# 使い方
# VoiceVox
デフォルトのユーザー辞書(voicevox本体のフォルダ/vv-engine/default.csv)をバックアップしておく。  
kanayomi-dict.csvをdefault.csvに名前を変更して置き換える。  
元のdefault.csvに入っているキャラの名前などは正しい読み方で読めなくなります。  

# 辞書の説明  
・en-kana系辞書  
openjtalkで使われているnaist-jdicかunidicのカタカナ語を抽出し英単語カタカナ辞書と合体させた辞書。  
英単語を日本語発音で読ませられるようになります。

・kana系辞書  
openjtalkで使われているnaist-jdicかunidicのカタカナ語を抽出しひらがなに直した辞書。 
ひらがなで記述されたカタカナ語を正しいアクセントで読めるようになる。

・mecab-ipadic-neologd系辞書  
mecab-ipadic-neologdにダミーのアクセントを付けた辞書  
人名や地名、駅名などを正しい読み方で読めるようになります。  

・kanayomi-dict  
上記の辞書を統合した物

# これからの予定  
以下の古い日本語入力用ユーザー辞書の追加  
麻雀用語辞書  
三国志人名辞書  
姓名辞書

# 使用させていただいたもの。  
英単語カタカナ変換ライブラリ  
https://github.com/zomysan/alkana.py  
mecab-ipadic-neologd  
https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md  
openjtalkに含まれていた辞書（以下のフォークのものを使用しました。）  
https://github.com/r9y9/open_jtalk  
