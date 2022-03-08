def SumarVector(vector,elemento):
    if elemento == 0:
        return vector[elemento]
    else:
        return SumarVector(vector,elemento-1)+vector[elemento]

vectorenteros = [1,2,3,4,5,6,7,8,9]
print("Vector de enteros: ", vectorenteros)
elementosasumar = int(input("¿Cuántos elementos quieres sumar?: "))
if (elementosasumar > 0) & (elementosasumar <= len(vectorenteros)):
    print("Resultado: ",SumarVector(vectorenteros,elementosasumar-1))
else:
    print("ERROR: El número de elementos a sumar es erróneo")
    