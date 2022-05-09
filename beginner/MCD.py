def mcd(numero1,numero2):
    if numero2 == 0:
         return numero1
    elif numero1 == 0:
        return numero2
    else:
        if numero1>numero2:
            return mcd(numero1-numero2, numero2)
        else:
            return mcd(numero1, numero2-numero1)
numeroleido1 = int(input("Primer número para calcular el MCD: "))
numeroleido2 = int(input("Segundo número para calcular el MCD: "))
print("Resultado MCD: " + str(mcd(numeroleido1,numeroleido2)))