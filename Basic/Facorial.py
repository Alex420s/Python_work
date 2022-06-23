def Factorial(numero):
    if numero == 1:
         return 1
    else:
        return numero * Factorial(numero-1)
factorial = int(input("Número a calcular el factorial: "))
print("Resultado: " + str(Factorial(factorial)))
