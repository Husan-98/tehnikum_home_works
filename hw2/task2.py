x = input("Введите слово и я угадаю палиндром ли он или нет : ")
ch = str()
for j in x:
     if j != " ":
        ch = ch + j
lch = len(ch)
if lch == 3 and ch[0] == ch[-1]:
    print("слово палиндром")
elif lch == 4 and ch[0] == ch[-1] and ch[1] == ch[-2]:
    print("слово палиндром")
elif lch == 5 and ch[0] == ch[-1] and ch[1] == ch[-2]:
    print("слово палиндром")
elif lch == 6 and ch[0] == ch[-1] and ch[1] == ch[-2] and ch[2] == ch[-3]:
    print("слово палиндром")
elif lch == 7 and ch[0] == ch[-1] and ch[1] == ch[-2] and ch[2] == ch[-3]:
    print("слово палиндром")
elif lch == 8 and ch[0] == ch[-1] and ch[1] == ch[-2] and ch[2] == ch[-3] and ch[3] == ch[-4]:
    print("слово палиндром")
elif lch == 9 and ch[0] == ch[-1] and ch[1] == ch[-2] and ch[2] == ch[-3] and ch[3] == ch[-4]:
    print("слово палиндром")
elif lch == 10 and ch[0] == ch[-1] and ch[1] == ch[-2] and ch[2] == ch[-3] and ch[3] == ch[-4] and ch[4] == ch[-5]:
    print("слово палиндром")
elif lch == 11 and ch[0] == ch[-1] and ch[1] == ch[-2] and ch[2] == ch[-3] and ch[3] == ch[-4] and ch[4] == ch[-5]:
    print("слово палиндром")
else:
    print("Слово не является палинромом")
