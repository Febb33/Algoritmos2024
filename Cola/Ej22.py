
from Cola import Queue

cola = Queue()

class Heroes:

    def __init__(self, nombre, heroe, sexo):
        self.nombre = nombre
        self.heroe = heroe
        self.sexo = sexo

    def __str__ (self):
        return f' {self.nombre} - {self.heroe} - {self.sexo} '

Personajes = [
    {'nombre': '89P13', 'heroe': 'Rocket Raccoon', 'sexo': 'M'},
    {'nombre': 'Tony Stark', 'heroe': 'Iron Man', 'sexo': 'M'},
    {'nombre': 'Steve Rogers', 'heroe': 'Capitan America', 'sexo': 'M'},
    {'nombre': 'Natasha Romanoff', 'heroe': 'Black Widow', 'sexo': 'F'},
    {'nombre': 'Loki', 'heroe': 'Loki', 'sexo': 'M'},
    {'nombre': 'Thor', 'heroe': 'Thor', 'sexo': 'M'},
    {'nombre': 'Bruce Banner', 'heroe': 'Hulk', 'sexo': 'M'},
    {'nombre': 'Nicholas Joseph Fury', 'heroe': 'Nick fury', 'sexo': 'M'},
    {'nombre': 'Peter Parker', 'heroe': 'Spider-Man', 'sexo': 'M'},
    {'nombre': 'Carol Danvers', 'heroe': 'Capitana Marvel', 'sexo': 'F'},
    {'nombre': 'Scott Lang', 'heroe': 'Ant-Man', 'sexo': 'M'},
]

def search (buscado):

    for i in range (cola.size()):

        if cola.on_front().heroe == buscado:
            return cola.on_front().nombre
            cola.move_to_end()
        else:
            cola.move_to_end()

def mostrar_nombres(s):

    for i in range (cola.size()):

        if cola.on_front().sexo == s:
            print(cola.on_front().nombre)
            cola.move_to_end()
        else:
            cola.move_to_end()

def inicial_s(ini):

    for i in range (cola.size()):

        if cola.on_front().nombre[0] == ini or cola.on_front().heroe[0] == ini:
            print(cola.on_front())
            cola.move_to_end()
        else:
            cola.move_to_end()


for Per in Personajes:
    cola.arrive(Heroes(Per['nombre'], Per['heroe'], Per['sexo']))

print()
for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()


# d
print()
buscado = 'Ant-Man'
print(f'{buscado} es {search(buscado)}')

# a y f
print()
buscado = 'Capitana Marvel'
print(f'{search(buscado)} es {buscado}')

# c
print()
sexo = 'M'
print('Nombres Masculinos:')
mostrar_nombres(sexo)

# b
print()
sexo = 'F'
print('Nombres Femeninos:')
mostrar_nombres(sexo)

# e
print()
inicial = 'S'
print('Iniciales S:')
inicial_s(inicial)
