word = "mkLeo"
pos = word.find('|') + 1
new_word = word[pos:]
stripped = new_word.strip()
print(stripped)
