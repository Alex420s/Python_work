DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 66,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
"""
Resuelve usando High order functions y list comrehensions:
Crea una lista nombrando, solo a quien use Python
Crea una lista con los trabajadores de Platzy
Crea una lista de personas mayores y otra con  mayores de edad,
Despues añade a los  diccionarios en DATA si es adulto o mayor de edad. 
"""
def run():
    only_Python =[worker ["name"] for worker in DATA if worker ["language"] == "python"]
    Platzi_workers = list(filter(lambda worker: worker ["organization"] == "Platzi", DATA))
    Platzi_workers = list(map(lambda worker: worker ["name"], Platzi_workers))
    Personas_mayores = list(filter(lambda worker: worker ["age"] > 65, DATA))
    Personas_mayores = list(map(lambda worker: worker ["name"], Personas_mayores))
    Adultos = list(map(lambda worker: worker | {"Adult": worker ["age"] > 18} | {"Old-man": worker ["age"] > 64}, DATA))

    print(only_Python,1)
    print(Platzi_workers,2)
    print(Personas_mayores,3)
    print(Adultos,4)
if __name__ == '__main__':
    run()
