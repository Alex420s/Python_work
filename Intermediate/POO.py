#defino la clase persona
class Persona:
    #método constructo de clase, se inicia al crear una instancia.
    #self hace referencia a la misma clase
    #indico que tipo de dato espero obtener en la variable edad (edad: int)
    #mediandte assert aseguro obtener un numero positivo en edad
    def __init__(self, edad: int, genero, nombre):
        "Variables de clase, representan información que es común para todas las instancias."
        assert edad >= 0, f"la edad {edad} no es valida, debe se mayor o igual a cero!"

        self.edad = edad
        self.genero = genero
        self.nombre =nombre
        self.respira = True
        self.hambre = 0
        self.energia= 100 - (edad*1.1) #Enegia al 73.6
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
    def __str__(self):
       return  print("Pequeño ejercicio libre sobre POO, aún no lo aplico a un proyecto")

Alex=Persona(24,"masculino", "Alexis")
Alex.ejercicio("leve")
Alex.comer("Arroz y frijoles con guisado")
Alex.ejercicio("mortal")
diego = Persona(4, "hermafrodita","Diego")
Alex.__str__()