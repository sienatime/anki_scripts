import codecs

def write_to_output(input_name, output_name):
  f = codecs.open(input_name, encoding="utf-8")
  lines = f.readlines()

  output = codecs.open(output_name, "w", encoding="utf-8")

  for line in lines:
    tokens = line.split()

    for token in tokens:
      # pdb.set_trace()
      start_bracket = token.find("[")
      if start_bracket > -1:
        end_bracket = token.find("]")
        length = len(token)

        output.write(token[:start_bracket])
        output.write(token[end_bracket+1:])
        output.write(";")
        output.write(token)
        output.write("\n")

  output.close()