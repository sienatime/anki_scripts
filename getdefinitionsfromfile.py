# -*- coding: utf-8 -*-

# used to insert meanings into a delimiter-separated list of notes
# (optional) Export from Anki (Notes) - use \t delimiter, or
# use output file from oneoff_makecards

# start python REPL from this file's location (run `python`)

# import getdefinitionsfromfile
# getdefinitionsfromfile.write_to_output("import.csv", "defs.tsv")

# if you make changes and need to reload:
# reload(getdefinitionsfromfile)

# format is tab-separated:
# 射的		射: shoot<br>的: bull's eye<br>	射的[しゃてき]
# the meaning needs to go after the first tab.

import requests
import codecs

def write_to_output(input_name, output_name):
  f = codecs.open(input_name, encoding="utf-8")
  lines = f.readlines()
  output_file = codecs.open(output_name, "w", encoding="utf-8")
  delimiter = "\t"

  jisho_api = u"http://jisho.org/api/v1/search/words?keyword="

  for line in lines:
    split_line = line.split(delimiter)
    expression = split_line[0].strip()
    jisho_response = requests.get(jisho_api + expression)

    if (len(jisho_response.json().get('data')) > 0):
      first_result = jisho_response.json().get('data')[0]
      words = all_search_term_results(first_result)

      if (expression in words):
        print("Searched for " + expression + ": " + words)
        split_line[1] = format_meaning(first_result)
        output_file.write(delimiter.join(split_line))
      else:
        print("No suitable matches found for " + expression)
        print("Got: " + words)

  output_file.close()

def all_search_term_results(result):
  return ", ".join([data.get('word') for data in result.get('japanese') if data.get('word')])

def format_meaning(result):
  meaning = ""

  for definition in result.get('senses'):
    meaning += ", ".join(definition.get('english_definitions'))
    meaning += "<br>"

  return meaning
