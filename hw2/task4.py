x = input()
ch = str()
for j in x:
     if j != " ":
        ch = ch + j
lch = len(ch)
new = str()
for i in range(lch - 1):
    if ch[i] != ch[i-1]:
        new = new + ch[i]
print(new + ch[-1])
