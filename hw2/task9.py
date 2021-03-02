a = input("Введите предложение и я угодаю сколько в нем слов : ")
     counter = 0
     for i in a:
         if i == " ":
             counter = counter + 1
     print("В предложение", counter + 1, "слов")
