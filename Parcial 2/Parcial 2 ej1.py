
from Arbol_avl import BinaryTree
from random import randint

Arbol_nombre = BinaryTree()
Arbol_numero = BinaryTree()
Arbol_tipo = BinaryTree()

Pokemons = [
   {
        "nombre": "Pikachu",
        "tipo": "Eléctrico",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Charizard",
        "tipo": "Fuego, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Bulbasaur",
        "tipo": "Planta, Veneno",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Starmie",
        "tipo": "Agua, Psíquico",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Psyduck",
        "tipo": "Agua",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Gyarados",
        "tipo": "Agua, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Onix",
        "tipo": "Roca, Tierra",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Geodude",
        "tipo": "Roca, Tierra",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Vulpix",
        "tipo": "Fuego",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Blastoise",
        "tipo": "Agua",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Umbreon",
        "tipo": "Siniestro",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Nidoking",
        "tipo": "Veneno, Tierra",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Dragonite",
        "tipo": "Dragón, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Aerodactyl",
        "tipo": "Roca, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Tyrantrum",
        "tipo": "Roca, Dragón",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Kakuna",
        "tipo": "Bicho, Veneno",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Vivilon",
        "tipo": "Bicho, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Slurpuff",
        "tipo": "Hada",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Roserade",
        "tipo": "Planta, Veneno",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Gabyte",
        "tipo": "Dragón, Tierra",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Celebi",
        "tipo": "Psíquico, Planta",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Vibrava",
        "tipo": "Tierra, Dragón",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Oranguru",
        "tipo": "Normal, Psíquico",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Ho-oh",
        "tipo": "Fuego, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Greninja",
        "tipo": "Agua, Siniestro",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Froslass",
        "tipo": "Hielo, Fantasma",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Surskit",
        "tipo": "Bicho, Agua",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Hoothoot",
        "tipo": "Normal, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Yamask",
        "tipo": "Fantasma",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Cosmog",
        "tipo": "Psíquico",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Marril",
        "tipo": "Agua, Hada",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Arceus",
        "tipo": "Normal",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Rampados",
        "tipo": "Roca",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Toxapex",
        "tipo": "Veneno, Agua",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Electabuzz",
        "tipo": "Eléctrico",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Terrakion",
        "tipo": "Roca, Lucha",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Wingull",
        "tipo": "Agua, Volador",
        "numero": randint(1, 99)
    },
    {
        "nombre": "Jolteon",
        "tipo": "Eléctrico",
        "numero": randint(1,99)
    },
    {
        "nombre": "Lycanroc",
        "tipo": "Roca",
        "numero": randint(1,99)
    }
]


# a
for Pokemon in Pokemons:
    Arbol_nombre.insert_node(Pokemon['nombre'], Pokemon)
    Arbol_numero.insert_node(Pokemon['numero'], Pokemon)
    Arbol_tipo.insert_node(Pokemon['tipo'], Pokemon)


# b
print()
print('Busqueda por número:')
buscado = Arbol_numero.search(randint(1, 99))
if buscado is not None:
    print(buscado.other_value)
else:
    print('No encontrado')


print()
print('Busqueda por nombre:')
value = Arbol_nombre.proximity_search_all_info('G')
if value is not None:
    print(value)


# c
print()
print('Pokemons de tipo Agua, Fuego, Planta y Eléctrico:')
Arbol_tipo.pokemons_tipos()


# d
print()
print("Listado ascendente por número:")
Arbol_numero.inorden_2()

print()
print("Listado ascendente por nombre:")
Arbol_nombre.inorden()

print()
print("Listado por nivel de nombre:")
Arbol_nombre.by_level()


# e
print()
buscado = Arbol_nombre.search("Jolteon")
if buscado is not None:
    print("Encontrado:", buscado.other_value)
else:
    print(f'No se encontró a {buscado}')

buscado = Arbol_nombre.search("Lycanroc")
if buscado is not None:
    print("Encontrado:", buscado.other_value)
else:
    print(f'No se encontró a {buscado}')

buscado = Arbol_nombre.search("Tyrantrum")
if buscado is not None:
    print("Encontrado:", buscado.other_value)
else:
    print(f'No se encontró a {buscado}')


# f
print()
print('Cantidad de pokemons de tipo Eléctrico:', Arbol_tipo.cont_tipo('Eléctrico'))

print()
print('Cantidad de pokemons de tipo Acero:', Arbol_tipo.cont_tipo('Acero'))

