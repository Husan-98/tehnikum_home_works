a = ["привет", "dsfsdfsdfsdf","дела"]

b = []
for i in a:
    b.append(len(i))
b = sorted(b)
b = b[-1]
for i in a:
    if len(i) == b:
        print(i)
    else:
        continue
