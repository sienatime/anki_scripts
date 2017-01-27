# generate Heisig keywords for a single card

# Open Anki REPL from Anki home screen with Cmd Shift : (colon)
# Paste script
# Change value of exp
# Hit Cmd Enter to run script

rtk = mw.col.findCards("tag:rtk1")
rtk3 = mw.col.findCards("tag:rtk3")

rtk.extend(rtk3)

rtkDict = {}

for id in rtk:
  card = mw.col.getCard(id)
  note = card.note()
  kanji = note.__getitem__(u'Expression')
  keyword = note.__getitem__(u'Keyword')
  rtkDict[kanji] = keyword

exp = u"剥き出し"

output = ""

for c in exp:
  if rtkDict.get(c):
    output += c + ": " + rtkDict.get(c) + "\n"

print output