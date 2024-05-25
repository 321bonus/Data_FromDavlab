word = input('')
loop = int(input())


if len(word) > loop:
    print(word[:loop] + '...')
else:
    print(word)
    