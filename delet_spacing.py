word = 'My feelings are overwhelmed by you.'
result_word = []
sp_word = []
for i in word:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        sp_word.append(i)
    elif i.strip() and i not in ('a','e','i','o','u','A','E','I','O','U'):
        result_word.append(i)

print(''.join(sp_word))
print(''.join(result_word))