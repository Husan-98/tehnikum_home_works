#поиск наибольшего числа 

a = float(input())
b = float(input())
c = float(input())
average = (a + b + c) - max(a, b, c) - min(a, b, c)
print((a + b + c) - average - min(a, b, c))

######################################################
#второй вариант 
a = float(input())
b = float(input())
c = float(input())
m = 0
if a >= m:
    m = a
if b > m:
    m = b
if c > m:
    m = c
print(m)
