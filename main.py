class Myname():
    person = 'john'

    def __init__(self, name, age):
        self.name = name
        self.age = age

person2 = Myname('Milk',4)
person3 = Myname('Mike',2)

print("{} is {} and {} is {}.".format(person2.name,person2.age,person3.name,person3.age))

if Myname.person == 'john':
    print("{} is a {}!".format(Myname.person, person2.age))