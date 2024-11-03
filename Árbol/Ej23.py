
from Arbol_avl import BinaryTree

tree = BinaryTree()

Creatures = [
    {
        "Criatura": "Ceto",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Tifón",
        "Derrotado": "Zeus",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Equidna",
        "Derrotado": "Argos Panoptes",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Pefredo",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Enio",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Escila",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Caribdis",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Euríale",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Esteno",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Medusa",
        "Derrotado": "Perseo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Ladón",
        "Derrotado": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Águila del Cáucaso",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Quimera",
        "Derrotado": "Belerofonte",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Hidra de Lerna",
        "Derrotado": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "León de Nemea",
        "Derrotado": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Esfinge",
        "Derrotado": "Edipo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Dragón de la Cólquida",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Cerbero",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Cerda de Cromión",
        "Derrotado": "Teseo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Ortro",
        "Derrotado": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Toro de Creta",
        "Derrotado": "Teseo",
        "Descripcion": None,
        "Capturada": None
    },
    {
        "Criatura": "Jabalí de Calidón",
        "Derrotado": "Atalanta",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Carcinos",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Gerión",
        "Derrotado": "Heracles",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Cloto",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Láquesis",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Átropos",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Minotauro de Creta",
        "Derrotado": "Teseo",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Harpías",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Argos Panoptes",
        "Derrotado": "Hermes",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Aves del Estínfalo",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Talos",
        "Derrotado": "Medea",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Sirenas",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Pitón",
        "Derrotado": "Apolo",
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Cierva de Cerinea",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Basilisco",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    },    
    {
        "Criatura": "Jabalí de Erimanto",
        "Derrotado": None,
        "Descripcion": None,
        "Capturada": None
    }
]


for Creature in Creatures:
    tree.insert_node(Creature['Criatura'], Creature)

# a
print()
tree.creatures_inorden()

# b
# for Creature in Creatures:
#     tree.insert_node(Creature['Criatura'], Creature['Derrotado'], Creature['Capturada'])

# c
print()
pos = tree.search('Talos')
if pos is not None:
    print(pos.other_value)

# d
# print()
# print(tree.contar_dioses_heroes())

# e
print()
print('Criaturas derrotadas por Heracles:')
tree.inorden_heracles_derrotada()

# f
print()
print('Criaturas no derrotadas:')
tree.inorden_no_derrotadas()

# g
# print()

# h
print()
# Bestias = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']
# for Bestia in Bestias:
#     tree.search(Bestia)
#     # tree.insert_node['Capturada'] = 'Heracles'
#     # print(tree.inorden(Bestias))
    

   

# i

# j
print()
# print(tree.proximity_search('Sirenas'))
# print(tree.proximity_search('Basilisco'))
value_to_delete = 'Sirenas'
for i in range(2):
    delete_value, extra_info = tree.delete_node(value_to_delete)
    print(f'Se eliminó: {value_to_delete}')
    value_to_delete = 'Basilisco'
# print(tree.proximity_search('Sirenas'))
# print(tree.proximity_search('Basilisco'))

# k
# print()

# l
print()
tree.proximity_search('La')
value_to_delete = 'Ladón'
delete_value, extra_info = tree.delete_node(value_to_delete)
print('Eliminado:', delete_value)
new_name = 'Dragón Ladón'
extra_info['Criatura'] = new_name
tree.insert_node(new_name, extra_info)
pos = tree.search('Dragón Ladón')
if pos is not None:
  print('Encontrado:', pos.other_value)
tree.proximity_search('Dra')

# m
print()
print('Listado por nivel:')
tree.by_level()

# n
print()
print('Criaturas capturadas por Heracles:')
tree.inorden_heracles_capturada()
