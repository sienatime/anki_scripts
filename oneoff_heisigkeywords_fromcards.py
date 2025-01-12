# Used to set Vocab Mega Deck Heisig keywords from existing Anki cards

# note that you can't define functions in the Anki REPL (ugh) so that's why this is just one long script

# Tag cards with "add_keywords"
# Open Anki REPL from Anki home screen with Cmd Shift : (colon)
# Paste script
# Hit Cmd Enter to run script
# Double-check output
# Tag "add_keywords" will be removed programmatically

# construct RTK dictionary, used for looking up Heisig keywords
# key is kanji, value is keyword, e.g.
# { 理: logic }

TAG_TO_FIND = "add_keywords"

rtk = mw.col.find_cards("tag:rtk1")
rtk3 = mw.col.find_cards("tag:rtk3")

rtk.extend(rtk3)

rtk_dict = {}

for id in rtk:
  card = mw.col.get_card(id)
  note = card.note()
  kanji = note.__getitem__(u'Expression')
  keyword = note.__getitem__(u'Keyword')
  rtk_dict[kanji] = keyword

# find cards by desired tag
card_ids = mw.col.find_cards("tag:" + TAG_TO_FIND)

# loop through card ids and set Heisig keywords field directly.
for id in card_ids:
  heisig_keywords = ""
  card = mw.col.get_card(id)
  note = card.note()
  expression = note.__getitem__(u'Expression')

  for character in expression:
    if rtk_dict.get(character):
      heisig_keywords += character + ": " + rtk_dict.get(character) + "<br>" # use <br> instead of newline because the newline delimits each entry instead

  note[u'Heisig keywords'] = heisig_keywords
  note.remove_tag(TAG_TO_FIND)
  mw.col.update_note(note)

num_cards = len(card_ids)
print(f"Modified {num_cards} card{'' if num_cards == 1 else 's'}")
