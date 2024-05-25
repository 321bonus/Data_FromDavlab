import random
# Random number 
number1 = random.randint(1,101)
print(number1)

# Random Word 2 word or more than 2 word
list_word = ['Iron man', 'Spiderman', 'Doctor streg']
tranfrom = random.sample(list_word,2)
print(tranfrom)
# Make it not list
test = ''
for i in tranfrom:
    test += i
print("tranform:",test, end="")

# Random 1 Word 
randoms1 = list_word
print(random.choice(randoms1))