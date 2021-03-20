strok = input("Введите строку : ")
integ = int(input("Введите кол-во повторений : (В ЦЕЛЫХ ЧИСЛАХ !)"))

f = open('hw_5file', mode='a')

for i in range(integ):
    f.write(strok + '\n')
