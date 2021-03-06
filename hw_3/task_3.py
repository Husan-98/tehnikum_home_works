one = float(input("Введите первое число : "))
oper = input("Введите операцию которую хотите выполнить (+, -, *, /) : ")
two = float(input("Введите второе число : "))
if oper == "+":
  print(one + two)
elif oper == "/" and two == 0:
  print("На ноль делить нельзя")
elif oper == "-":
  print(one - two)
elif oper == "*":
  print(one * two)
elif oper == "/":
  print(one / two)
else:
  print("Error")
