from Person import Person
from Manager import Manager

p1 = Person('a1', 11, 200, 'py')
p2 = Person('a2', 12, 202, 'py')
print(p1.lastName())
print(p2.lastName())
print(p1.pay)
print(p2.pay)
p1.giveRaise(0.5)
p2.giveRaise(0.6)
print(p1.pay)
print(p2.pay)
m1 = Manager('k1', 50, 600, 'py')
print(m1.pay)
m1.giveRaise(0.5)
print(m1.pay)
