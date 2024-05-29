
from Pila import Stack
pila = Stack()

class Personaje:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas
    
    def __str__(self):
        return f"{self.nombre} {self.cantidad_peliculas}"

Personajes = [
    {'nombre': 'Rocket Raccoon', 'cant_pelis':4},
    {'nombre': 'Iron Man', 'cant_pelis':6},
    {'nombre': 'Capitan America', 'cant_pelis':5},
    {'nombre': 'Groot', 'cant_pelis':4},
    {'nombre': 'Black Widow', 'cant_pelis':7},
    {'nombre': 'Loki', 'cant_pelis':4},
    {'nombre': 'Thor', 'cant_pelis':8},
    {'nombre': 'Hulk', 'cant_pelis':9},
    {'nombre': 'Nick fury', 'cant_pelis':11},
]

for Per in Personajes:
    pila.push(Personaje(Per['nombre'], Per['cant_pelis']))

Iniciales = ['C', 'D', 'G']
pos = pila.size()

while pila.size() != 0:
    dato = pila.pop()

    if dato.nombre == "Rocket Raccoon" or dato.nombre == "Groot":
        print()
        print(dato.nombre, "se encuentra en la posicion", pos)

    if dato.nombre == "Black Widow":
        print()
        print("Black Widow participó en", dato.cantidad_peliculas, "peliculas")

    if dato.cantidad_peliculas > 5:
        print()
        print("Personaje más de 5 peliculas:", dato)
        
    if dato.nombre[0] in Iniciales:
        print()
        print("Personajes inicial C, D, G:", dato.nombre)
