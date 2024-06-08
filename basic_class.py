class digit():
    def __init__(self):
        self.num1 = int(input())
        self.num2 = int(input())
        self.word = input()

    def plust(self):
        return self.num1 + self.num2
    def minus(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divis(self):
        return self.num1 / self.num2
    
cal = digit()
if cal.word == '+':
    print(f"{cal.num1} + {cal.num2} = {cal.num1 + cal.num2}")