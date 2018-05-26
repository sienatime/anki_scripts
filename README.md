Making New Cards
================
1. Start with `oneoff_makecards.py`. This script takes a list of words and generates a semi-colon-separated list that has expression, Heisig keywords, and reading. Meaning is left blank.
2. Import the new cards into Anki
2. Put the same list through `getdefinitions.py`. This will print English definitions out to the console from the Jisho.org API. Manually add definitions to the cards in Anki (it can be a little impresise/return multiple results, and that's why it's not automated).
