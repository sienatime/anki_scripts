# -*- coding: utf-8 -*-

# source env/bin/activate
# python getreadings.py
# deactivate

import requests

input = u"""
麻痺
胡散
"""

expressions = input.split()
jisho_api = u"http://jisho.org/api/v1/search/words?keyword="

for expression in expressions:
  jisho_response = requests.get(jisho_api + expression)

  if (len(jisho_response.json().get('data')) > 0):
    first_result = jisho_response.json().get('data')[0]
    # print out what word we're getting definitions for, just in case
    print ", ".join([data.get('word') for data in first_result.get('japanese') if data.get('word')])
    output = ""

    for definition in first_result.get('senses'):
      output += ", ".join(definition.get('english_definitions'))
      output += "\n"

    print output