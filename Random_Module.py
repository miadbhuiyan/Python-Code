import random
a = random.randint(1,3)
print(a)
b = random.randrange(1,3)
print(b)
l=[2,-2,4,6,67,45,23]
c = random.choice(l)
print(c)
d = random.random()
print(d)
e=[34,209,34,5,234,45,98,34,54]
random.shuffle(e)
print(e)