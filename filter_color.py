import re

word = input().split()

tranform = [re.findall(r"\w+", w)for w in word]

flattend_tranform = [item for sublist in tranform for item in sublist]

red = 0
green = 0
blue = 0
white = 0
black = 0

for i in flattend_tranform:
    if i == 'red':
        red += 1
    elif i == 'green':
        green += 1
    elif i == 'blue':
        blue += 1
    elif i == 'white':
        white += 1
    elif i == 'black':
        black += 1

print(f"red = {red}, green = {green}, blue = {blue}, white = {white}, black = {black}")