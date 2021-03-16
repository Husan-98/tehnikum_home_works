a = 'привет как дела'
a = a.split(' ')

b = []
for i in a:
    b.append(len(i))

b = max(b)
for i in a:
    if b == len(i):
        print(i)
    else:
        continue
