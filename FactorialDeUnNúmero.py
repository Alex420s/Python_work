numero = int(input("Insterte un numero y dare el factorial: "))
def factorial (numero):
    if numero == 1:
        return 1
    else:   
        return numero * factorial(numero-1)
resultado = factorial (numero)
print(f"El factorial de {numero} es {resultado}")