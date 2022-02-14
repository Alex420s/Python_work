#Es posible insertar una lista dentro de un diccionario. Para acceder a cada uno de los cursos usamos los índices:
diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }
print(diccionario ['cursos'] [0])
print(diccionario ['cursos'] [1])
print(diccionario ['cursos'] [2])
#Para recorrer todo el diccionario usamos l estructura for:
for key in diccionario:
  print(key, ":", diccionario[key])
#Recibe como parámetro una representación de un diccionario y si es factible, devuelve un diccionario de datos.
dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)
print(dic)
""" Recibe dos elementos iterables: cadena, lista o tupla. Ambos deben tener el mismo número de elementos.
    Devolverá un diccionario relacionando el elemento  de cada uno de los iterables."""
diczip = dict(zip('abcd',[1,2,3,4]))
print(diczip)
#Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
print(dic.items())
#Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
print(dic.keys())
#Retorna una lista de elementos, que serán los valores de nuestro diccionario.
print(dic.values())
#Borra TODO el contenido
dic1 = {"a" : "1","b" : "2", "c" :"3" ,"d" : "4"}
dic1.clear()
print(dic1)
#Copia los elementos de un diccionario en uno nuevo.
Dic2=diccionario.copy()
print(Dic2)
"""Recibe un iterable y un valor "X", 
devolviendo un diccionario que contiene como claves elementos del iterable con el mismo valor ingresado.
Si el valor no es ingresado, devolverá none para todas las claves.
No imprime claves repetidas."""

dic = dict.fromkeys(['w','e','e','d'],)
print(dic)
#regresa el valor de la clave, de no existir devuelve none
print(diccionario.get("edad"))
#Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.
print(dic.pop("e"))
#setdefault()
    #Funciona de dos formas. En la primera como get
Forma1=dic.setdefault("d")
    #Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.
Forma2=dic.setdefault("s",420)
print(Forma1)
print(dic)
"""Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida; 
si no hay claves iguales, este par clave-valor es agregado al diccionario."""
dic.update(diccionario)
print(dic)
#permite acceder a un valor especifico del diccionario mediante su clave.
print(dic["w"])
dic["w"] = "sak"
print(dic["w"])
#devuelve True si la clave esta en el diccionario versiones, de lo contrario devuelve False.
sak= (1,2,3)
print(5 in sak, 3 in sak)