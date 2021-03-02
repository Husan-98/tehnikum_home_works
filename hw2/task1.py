a = input("Составить из букв введенной строки слова")
s = str()
for i in a:
    if i != " ":
        s = s + i
if "и" in s and "з" in s and "о" in s and "б" in s and "р" in s and "е" in s and "т" in s and "а" in s and "т" in s and "е" in s and "л" in s and "ь" in s:
    print("В слове", s, "есть необходимые буквы чтобы собрать слово", "изобретатель")
if "г" in s and "о" in s and "р" in s and "а" in s:
    print("В слове", s, "есть необходимые буквы чтобы собрать слово", "гора")
if "з" in s and "в" in s and "е" in s and "р" in s and "ь" in s:
    print("В слове", s, "есть необходимые буквы чтобы собрать слово", "зверь")
if "с" in s and "т" in s and "у" in s and "л" in s:
    print("В слове", s, "есть необходимые буквы чтобы собрать слово", "стул")
if "а" in s and "р" in s and "б" in s and "у" in s and "з" in s:
    print("В слове", s, "есть необходимые буквы чтобы собрать слово", "арбуз")
if "п" in s and "р" in s and "и" in s and "в" in s and "е" in s and "т" in s:
    print("В слове", s, "есть необходимые буквы чтобы собрать слово", "привет")
if "к" in s and "о" in s and "ш" in s and "к" in s and "а" in s:
    print("В слове", s, "есть необходимые буквы чтобы собрать слово", "кошка")
