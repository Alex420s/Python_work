def Potencia(base,exponente):
    if exponente <= 0:
        return 1
    else:
        return base * Potencia(base,exponente-1)
base = int(input("Base de la potencia: "))
exponente = int(input("Exponente de la potencia: "))
print("Resultado: " + str(Potencia(base,exponente)))