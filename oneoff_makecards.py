# Used to generate Vocab Mega Deck cards from a list of words

# Card format is tab-delimited by field name, e.g.
# expression	meaning	heisig keywords	reading
# `meaning` is left blank because we can't make network requests, but you can export the cards and run
# getdefinitionsfromfile.py to hit the jisho.org API for them.

# heisig keywords need to be looked up in the rtk dictionaries

# note that you can't define functions in the Anki REPL (ugh) so that's why this is just one long script

# Open Anki REPL from Anki home screen with Cmd Shift : (colon)
# Paste script
# Change value of input
# Hit Cmd Enter to run script
# Save output to a text file
# Import text file into Anki via File -> Import (be sure to allow HTML in fields)
# Double-check output (especially mecab-generated readings), add definitions if desired

import codecs
japanese = __import__("3918629684")

# construct RTK dictionary, used for looking up Heisig keywords
# key is kanji, value is keyword, e.g.
# { 理: logic }

rtk = mw.col.find_cards("tag:rtk1")
rtk3 = mw.col.find_cards("tag:rtk3")

rtk.extend(rtk3)

rtk_dict = {}

for id in rtk:
  card = mw.col.getCard(id)
  note = card.note()
  kanji = note.__getitem__(u'Expression')
  keyword = note.__getitem__(u'Keyword')
  rtk_dict[kanji] = keyword

# define input (change this to the values you want)

input = u"""
自信満々
目迷五色
痛快無比
一進一退
玉石混交
単刀直入
電光石火
心機一転
社交辞令
誠心誠意
意気投合
意味不明
創意工夫
一国一城
天下無敵
自給自足
難行苦行
言語道断
起死回生
一部始終
絶体絶命
大義名分
八方美人
有言実行
門外不出
異口同音
臨機応変
異体同心
自画自賛
相乗効果
大同小異
天変地異
自己暗示
直射日光
明鏡止水
金科玉条
一刻千金
表裏一体
急転直下
空前絶後
敬天愛人
公私混同
大器晩成
痛快無比
我田引水
忠君愛国
私利私欲
臨命終時
居安思危
一言片句
異口同辞
安分守己
文従字順
我利私欲
深層心理
七難八苦
強悪強善
創業守成
解衣推食
天孫降臨
残編断簡
一刻千秋
居安思危
半信半疑
有頂天外
二律背反
入郷従郷
針小棒大
公私混同
空理空論
射将先馬
同仁一視
多事多難
一意専心
質疑応答
伝家宝刀
単純明快
机上空論
延命息災
印象批評
大樹美草
灯紅酒緑
科挙圧巻
生死存亡
安宅正路
異曲同工
創意工夫
夏虫疑氷
一心不乱
一味徒党
開源節流
聖人君子
応急処置
専心専意
量体裁衣
独断専行
息災延命
忠孝両全
清風朗月
縮地補天
孫康映雪
感奮興起
修己治人
装模作様
言易行難
三尺秋水
機略縦横
情意投合
三千世界
独立独歩
共存共栄
危急存亡
面従後言
困知勉行
異人同辞
寸歩難行
美意延年
悪婦破家
人事考課
全知全能
老成円熟
群疑満腹
救世済民
骨肉相食
縮衣節食
裁断批評
節衣縮食
一暴十寒
他力本願
残念至極
無我夢中
千金一刻
波乱曲折
南無三宝
満城風雨
名存実亡
一枚看板
以毒制毒
苦学力行
一視同仁
創業守文
純一無雑
混水模魚
独立自尊
三界火宅
三寸不律
至高至上
安心立命
多情多感
不得要領
諸行無常
安居危思
胸中成竹
臨終正念
傷天害理
至道無難
専心一意
九死一生
七転八起
以心伝心
舌先三寸
無理算段
薬九層倍
適者生存
眼光紙背
立身処世
至高無上
四神相応
十人十色
物我一体
三蔵法師
賛否両論
経世済民
寸進尺退
追本究源
湯池鉄城
片利共生
風雲人物
不老不死
一治一乱
諸子百家
無理難題
至公至平
出処進退
治乱興亡
寸馬豆人
仁者楽山
因小失大
曲直分明
同始異終
医食同源
長生久視
衆生済度
党利党略
公平無私
大腹便便
相思相愛
温故知新
量入制出
減収減益
異国情調
諸法無我
面従腹背
立命安心
一心一意
開口一番
一言一句
右往左往
有情非情
悪事千里
頭寒足暖
読書亡羊
暗雲低迷
一日片時
一世一代
意味深長
天下一品
生死肉骨
暴飲暴食
横説縦説
全身全意
飲河満腹
疑行無名
悪逆非道
明来暗往
一挙両得
強悪非道
正当防衛
油断大敵
未来永久
行雲流水
一片氷心
安家楽業
興味本位
一件落着
一路平安
因果応報
多種多様
百発百中
自作自演
生知安行
平身低頭
縦横自在
仁者無敵
意思表示
一心同体
一衣帯水
酒池肉林
文武両道
黄金時代
異口同声
不解衣帯
風林火山
一文不通
永世中立
夏下冬上
破顔一笑
太平無事
海約山盟
至理名言
極悪非道
危言危行
年功序列
笑比河清
則天去私
一挙一動
花鳥風月
四苦八苦
問答無用
富国強兵
三寒四温
天理人欲
天然自然
真実一路
論功行賞
一言半句
三日天下
利害得失
古今東西
低頭平身
自業自得
王政復古
有名無実
古往今来
悪逆無道
一字千金
文明開化
起承転結
無病息災
善後処置
天地無用
不可思議
一子相伝
牛歩戦術
悪口雑言
精神統一
過小評価
弱肉強食
二束三文
平安無事
"""

expressions = input.split()
output = ""
delimiter = "\t"

# loop through expressions and construct the semicolon-delimited string
for expression in expressions:
  output += expression
  output += delimiter
  output += delimiter # meaning is blank
  for character in expression:
    if rtk_dict.get(character):
      output += character + ": " + rtk_dict.get(character) + "<br>" # use <br> instead of newline because the newline delimits each entry instead
  output += delimiter
  output += japanese.reading.mecab.reading(expression)
  output += "\n"

print(output)
