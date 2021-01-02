# -*- coding: utf-8 -*-

# used to generate a file of cloze-style expressions, from the format of a VMD card
# to the format of a Cloze card.

# start python REPL from this file's location (run `python`)

# import generate_cloze
# generate_cloze.go("yojicloze.txt", "cloze.tsv")

import codecs

def go(input_name, output_name):
  f = codecs.open(input_name, encoding="utf-8")
  lines = f.readlines()
  output_file = codecs.open(output_name, "w", encoding="utf-8")
  delimiter = "\t"

  for line in lines:
    # expression | meaning | heisig keywords | reading
    split_line = line.split(delimiter)
    expression = split_line[0]
    clozed = ""
    for i in range(len(expression)):
      # {{c1::自}}{{c2::信}}{{c3::満}}{{c4::々}}
      char = expression[i]
      clozed += "{{c" + str(i + 1) + "::" + char + "}}"

    # cloze format is expression | reading | notes
    meaning = split_line[1].strip()
    # some meanings are blank
    if (len(meaning) > 0):
      # some meanings already end in a break
      if (meaning.endswith("<br>")):
        meaning += "<br>"
      else:
        meaning += "<br><br>"
    notes = meaning + split_line[2]
    cloze_card = [clozed, split_line[3].strip(), notes + "\n"]
    output_file.write(delimiter.join(cloze_card))

  output_file.close()
