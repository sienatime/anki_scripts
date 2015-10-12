# -*- coding: utf-8 -*-
# read lines from file, they look like this:
# 飯[めし];ご 飯[はん]
# 飲[の]む;飲酒[いんしゅ];飲食[いんしょく]
# 飼[か]う;飼育[しいく]
# 飽[あ]きる;飽食[ほうしょく];飽和[ほうわ]
# 飾[かざ]る;服飾[ふくしょく]
# 餅[もち];煎餅[せんべい]

# generate a string contain an expression (the string with all [] parts removed) and the reading, e.g.
# 鳶が鷹を生む;鳶[とび]が 鷹[たか]を 生[う]む

# some words contain multiple brackets, like u"鳶[とび]が 鷹[たか]を 生[う]む"
# so... you're gonna have to deal with that.

import codecs
import pdb

def remove_multi_brackets(reading):
  start = reading.find('[')
  if start == -1:
    return reading
  else:
    end = reading.find(']')
    return remove_multi_brackets(reading[:start] + reading[end+1:])

def main():
  f = codecs.open("vocabwordsrtk3.csv", encoding="utf-8")
  lines = f.readlines()

  output = codecs.open("vmdrtk3_seed.txt", "w", encoding="utf-8")

  for line in lines:
    readings = line.split(";")

    for reading in readings:
      expression = remove_multi_brackets(reading)

      output.write(expression.replace(" ", "").strip())
      output.write(";")
      output.write(reading.strip())
      output.write("\n")

  output.close()

if __name__ == "__main__":
  main()