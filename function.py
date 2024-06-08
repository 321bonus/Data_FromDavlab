def plust(a,b):
    return a+b

sum = plust(5,10)
print(sum)

def plus(a,b):
    print("a =", a)
    print('b =', b)
    print(a + b)
    return a + b

plus(1,2)

def hello():
    name = input()
    if name:
        print('Hello'+ str(name))
    else:
        print('Empty')

hello()