
from random import randint, choice
from datetime import time
from Heap import HeapMax

class Mision:
    def __init__(self, nivel, encargado, descripcion, hora, cant_storm):
        self.nivel = nivel
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.cant_storm = cant_storm

    # igual al __str__ pero para desarrolladores
    def __repr__(self):
        return (f"Mision (Nivel: {self.nivel}, Encargado: {self.encargado}, "
                f"Descripción: {self.descripcion}, Hora: {self.hora}, "
                f"Cantidad de Storm: {self.cant_storm})")
    
    # Forma de interactuar de dos objetos, aca dice que uno es mas grande que el otro
    def __lt__(self, other):
        return self.nivel < other.nivel  


Misiones = []
h = HeapMax()
Encargado = ['Generales', 'Phasma', 'Kylo Ren', 'Snoke']
Descrip = ['Ataque', 'Reconocimiento', 'Defensa', 'Revision', 'Limpieza']


for i in range(2):
    nivel = 3
    encargado = Encargado[3]
    descripcion = choice (Descrip)
    hora = time (randint(0, 23), randint(0, 59))
    cant_storm = randint(0, 100)
    Misiones.append(Mision (nivel, encargado, descripcion, hora, cant_storm))

for i in range(4):
    nivel = 2
    encargado = Encargado[2]
    descripcion = choice (Descrip)
    hora = time (randint(0, 23), randint(0, 59))
    cant_storm = randint(0, 100)
    Misiones.append(Mision (nivel, encargado, descripcion, hora, cant_storm))

for i in range(4):
    nivel = 1
    encargado = Encargado[0]
    descripcion = choice (Descrip)
    hora = time (randint(0, 23), randint(0, 59))
    cant_storm = randint(0, 100)
    Misiones.append(Mision (nivel, encargado, descripcion, hora, cant_storm))


for mision in Misiones:
    h.add(mision)


print()
for i in range(len(h.elements)):  
    print(f"Atendiendo misión {i + 1}: {h.atention()}")
    print()


    if i == 4:
        print('Misión solicitada por Phasma:')
        nueva_mision = Mision(2, 'Phasma', 'Revisión de intrusos en el hangar B7', time(randint(0, 23), randint(0, 59)), 25)
        h.add(nueva_mision)
        print("Misión agregada:", nueva_mision)
        print()


    if i == 5:
        print('Misión solicitada por Snoke:')
        nueva_mision = Mision(3, 'Snoke', 'Destruir el planeta Takodana', time(randint(0, 23), randint(0, 59)), randint(0, 100))
        h.add(nueva_mision)
        print("Misión agregada:", nueva_mision)
        print()

