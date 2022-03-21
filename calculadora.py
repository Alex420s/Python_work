num1=float(input("Escribe un número: "))
op = input("Escribe el operador: ")
num2 =float(input("Escribe el segundo número: "))
if op == "+":
    print (num1+num2)
elif op =="/":
    print (num1/num2)
elif op == "*":
    print (num1*num2)
elif op == "-":
    print(num1-num2)
else:
    print("Operdor invalido.")