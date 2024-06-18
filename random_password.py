import random
import string
characters = string.ascii_letters + string.digits + string.punctuation

word = random.randint(5,20)
random_chars = random.choices(characters, k=word)
random_num = random.randint(1,20)
result = ''.join(random_chars) + str(random_num)

print(''.join(result),'\t',''.join(random_chars))

list_password = ['Bonus123']
list_result = []

characters1 = string.ascii_letters + string.digits + string.punctuation
species = string.punctuation 

for i in list_password:
    num = random.randint(1,10)
    sp = ''.join(random.choices(species, k=num))
    word = ''.join(random.sample(i, min(5, len(i))))
    result = str(num) + word + sp

print(result)

list_word = ['123bonus']

for i in list_word:
    tranform = list(i)
    random.shuffle(tranform)
    result = ''.join(tranform)

print(result)