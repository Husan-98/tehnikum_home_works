import random
a = input()
a = list(a)
b = []
for i in a:
    if i != ' ':
        b.append(i)
res = random.sample(b, len(b)) 
for i in res:
    print(i, end='')
ser = random.sample(b, len(b)) 
print()
for i in ser:
    print(i, end='')
sre = random.sample(b, len(b)) 
print()
for i in sre:
    print(i, end='')
