
from Cola import Queue

cola = Queue()

class Per:

    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__ (self):
        return f' {self.nombre} - {self.planeta} '

Personajes = [
    {'nombre': 'Yoda', 'planeta': 'Dagobah'},
    {'nombre': 'Luke Skywalker', 'planeta': 'Tatooine'},
    {'nombre': 'Han Solo', 'planeta': 'Corellia'},
    {'nombre': 'Jar Jar Binks', 'planeta': 'Naboo'},
    {'nombre': 'Almirante Ackbar', 'planeta': 'Endor'},
    {'nombre': 'Ahsoka Tano', 'planeta': 'Shili'},
    {'nombre': 'Anakin Skywalker', 'planeta': 'Tatooine'},
    {'nombre': 'Chewbacca', 'planeta': 'Kashyyyk'},
    {'nombre': 'Leia Organa', 'planeta': 'Alderaan'},
    {'nombre': 'Boba Fett', 'planeta': 'Kamino'},
    {'nombre': 'Teek', 'planeta': 'Endor'},
    {'nombre': 'Jan Ors', 'planeta': 'Alderaan'},
    {'nombre': 'Mercurial Swift', 'planeta': 'Corellia'},
    {'nombre': 'Vane', 'planeta': 'Shili'},
    {'nombre': 'Wicket W. Warrick', 'planeta': 'Endor'},
]


def planetas (planet):

    for i in range (cola.size()):

        if cola.on_front().planeta == planet:
            print(cola.on_front().nombre)
            cola.move_to_end()
        else:
            cola.move_to_end()

def search (buscado):

    for i in range (cola.size()):

        if cola.on_front().nombre == buscado:
            return cola.on_front().planeta
            cola.move_to_end()
        else:
            cola.move_to_end()


for Pj in Personajes:
    cola.arrive(Per(Pj['nombre'], Pj['planeta']))

print()
for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()

# a
for i in range (3):
    if i == 1:
        print()
        planeta = 'Tatooine'
        print('Planeta Tatooine:')
        planetas(planeta)
    elif i == 2:
        print()
        planeta = 'Alderaan'
        print('Planeta Alderaan:')
        planetas(planeta)
    else:
        print()
        planeta = 'Endor'
        print('Planeta Endor:')
        planetas(planeta)

# b
print()
for i in range (2):
    if i == 0:
        buscado = 'Han Solo' 
        print(f'Nombre: {buscado} Planeta: {search(buscado)}')
    else:
        buscado = 'Luke Skywalker'
        print(f'Nombre: {buscado} Planeta: {search(buscado)}')

# c
print()
search('Yoda')
cola.arrive(Per('Onyx Cinder', 'Shili'))
cola.move_to_end()

for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()

# d
print()
for i in range(cola.size()-1):
    if cola.on_front().nombre == 'Jar Jar Binks':
        cola.move_to_end()
        cola.attention()
    else:
        cola.move_to_end()

for i in range(cola.size()):
    print(cola.on_front())
    cola.move_to_end()
