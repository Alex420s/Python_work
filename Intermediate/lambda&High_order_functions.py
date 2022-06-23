"""
Características principales de una función anónima:

*Son funciones que pueden recibir cualquier número de parámetros pero una única expresión, es evaluada y devuelta.
*Se puede usar en cualquier lugar en el que sea requerida.
*Se suelen usar en combinación con otras funciones, generalmente como argumentos de otra función.
"""
#Ejemplo sin lambda
#Usando Docstring.
def cuad(x):
    """Función cuadrado de un numero: 
    cuad(x) 
    returns x ** 2
"""
    return x**2
print(cuad(6))

#Ejemplo con lambda.

cuadrado = lambda x: x ** 2
print(cuadrado(5))

"""En el ejemplo anterior, x es el parámetro y x ** 2 la expresión que se evalúa y se devuelve.
la función no tiene nombre y se asigna al identificador cuadrado.
Al usar Lambda function ahorramos codigo y evitamos crear una nueva función, de este modo evitamos uso de memria inecesario.
"""
#La función map() en Python aplica una función a cada uno de los elementos de una lista.
#map(una_funcion, objeto_iterable)
"""
Imagina que tienes una lista de enteros y quieres obtener una nueva lista con el cuadrado de cada uno de ellos.
Seguramente, lo primero que se te ha ocurrido es algo similar a lo siguiente:
"""
enteros = [x for x in range(-1,10)]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)
print(cuadrados)

#Sin embargo, podemos usar una función anónima en combinación con map() para obtener el mismo resultado de una manera mucho más simple:

enteros = [x for x in range(21) if x % 2 == 0]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados)
#Se vuelve todavía más interesante cuando, en lugar de una lista de valores, pasamos como segundo parámetro una lista de funciones:

enteros = [x for x in range(-2,10)]
print(enteros)
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3
funciones = [cuadrado, cubo]
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)
"""
La función filter() filtra una lista de elementos para los que una función devuelve True.

    filter(una_funcion, una_lista)

Ejemplo:
Filtrar una lista de números para obtener solo los valores pares(sin lfilter).
"""
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(pares)

#No obstante, podemos usar la función filter() y una función lambda para obtener el mismo resultado con una sola línea de código:

valores = [x for x in range(11)]
pares = list(filter(lambda x : x % 2 == 0, valores))
print(pares)

#Reduce
"""
Esta función se utiliza para llevar un cálculo acumulativo sobre una lista de valores y devolver el resultado.

**La función reduce() está incluida en el módulo functools.
Ejemplo:
Imagina que quieres obtener el resultado de sumar todos los elementos de una lista.
Como en las veces anteriores, la suma la puedes calcular de la siguiente manera(sin reduce()):"""

valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el
print(suma)
#Pero también usando la función reduce() en combinación con una función lambda:
from functools import reduce
valores= [x for x in range(-2,3)]
suma =reduce(lambda x, y: x + y, valores)
print(suma)
