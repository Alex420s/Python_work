import csv 
#defino la clase persona
class Persona:
    #método constructo de clase, se inicia al crear una instancia.
    #self hace referencia a la misma clase
    #indico que tipo de dato espero obtener en la variable edad (edad: int)
    #mediandte assert aseguro obtener un numero positivo en edad

    all=[]# Declaramos una lista con las intancias creadas.
    def __init__(self, edad: int, genero, nombre):
        "Variables de clase, representan información que es común para todas las instancias."
        assert edad >= 0, f"la edad {edad} no es valida, debe se mayor o igual a cero!"

        self.edad = edad
        self.genero = genero    
        self.nombre =nombre
        self.respira = True
        self.hambre = 0
        self.energia= 100 - (edad*1.1) #Enegia al 73.6
        #Añadimos cada instancia creada a la variable all
        Persona.all.append(self)

    def comer (self, comida):
        self.comida = comida
        if self.hambre > 60:
            print("Ya he comido , Gracias.".format(self.comida))
        else:
            print("Gracias por darme {}, no habia comido.".format(self.comida))
            self.hambre +=30
            self.energia +=15

    def ejercicio(self,intensidad):
        if self.energia == 0 or self.hambre == 0:
            print("Imposible, dejame descansar o dame de comer.")
        else: 
            if intensidad == "bajo":
              print("Un pequeño calentamiento")
              self.energia -15
              self.comida -10
            elif intensidad== "moderado":
               print("Ahora si sude.")
               self.energia - 25
               self.comida -15
            else:
                print("ese entrenamiento fue mortal.")
                self.energia -40
                self.hambre -35

    #representa al objeto con un tipo str de forma "bonita" para que el lector pueda entender.(informal)
    def __str__(self):
        return  f"Pequeño ejercicio libre sobre POO, aún no lo aplico a un proyecto"

    #representamos el objeto creado con un str de la manera mas fiel posible y que entiendan otros programadores.(oficial)
    def __repr__(self) -> str: 
        return f"Persona({self.edad},'{self.genero}','{self.nombre}')" #cambia la forma de representar nuestros objetos a TIPO STRING. "valid python code"
    #This method could not be called from an instance.
    """
    The class method is a method that are called on the class itself, not on a specific object instance. 
    Therefore, it belongs to a class level, and all class instances share a class method.
    """
    @classmethod
    def instanciate_from_csv(cls):#the class object itself is passed as the first argument  
        with open('Intermediate/inventario.csv', 'r') as f:
            #convierte el csv  diccionario python
            reader = csv.DictReader(f)
            #ahora lo convertimos a lista
            items = list(reader)
        for item in items:
            Persona(
                edad =float(item.get('Edad')),
                genero = item.get('Genero'),
                nombre =item.get('Nombre'),
            )
Persona.instanciate_from_csv()
print(Persona.all)
    


    
Alex=Persona(24,"masculino", "Alexis")
Alex.ejercicio("leve")
Alex.comer("Arroz y frijoles con guisado")
Alex.ejercicio("mortal")
diego = Persona(4, "hermafrodita","Diego")
print(Alex.__dict__)#muestra los atributos de instancia
#print(Persona.__dict__)# muestra los atributos de clase
print(Alex)
for instancia in Persona.all:
    print(instancia.edad,instancia.nombre)
print(Persona.all)

"""
Heredamos de Persona.
"""
class Padre(Persona):
    all=[]
    def __init__(self,edad: int, genero, nombre, hijos = True, soltero = True):
        #Call super function to have access to all attributes / methods
        super().__init__(edad, genero, nombre)
        #Run validations to te received arguments
        assert hijos == True or hijos == False, f"solo se admite True or False"
        # Assign to self object
        self.__soltero = soltero
        self._hijos = hijos
        #No deberiamos permitir que se modifiquen ciertos elementos de la clase, usaremos el encapsulamiento para impedirlo. 
        # Creamos un atributo de solo lectura mediante @property   
    # Property decorator = Read_Only Atribute
    @property
    def hijos(self):
        return self._hijos
    #definimos esta variable como privada pero despues permiti que pudieran caambiarlo mediante un setter.
    @property
    def soltero(self):
        return self.__soltero
    @soltero.setter
    def soltero(self, value):
        self.__soltero = value
        

          


Alexis=Padre(24,"Masculino", "Alexis", False, True)
print(Alexis.hijos)

Alexis.ejercicio("leve")
Alexis.comer("Patatas")
Alexis.ejercicio("leve")
print(Alexis.energia)
Alexis.soltero = False
print(Alexis.soltero)
print(Alexis.hijos)