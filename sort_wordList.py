list_word = ['python','java','javascript']

record = map(len, list_word)

word = list(record)

word.sort

print(word)

sorteds = sorted(list_word, key=len)

print(sorteds)