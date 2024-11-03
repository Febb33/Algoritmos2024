
from Grafo import Graph

grafo = Graph(dirigido = False)

Casa = [
    "Cocina", "Comedor", "Cochera", "Quincho",
    "Baño 1", "Baño 2", "Habitación 1", "Habitación 2",
    "Sala de estar", "Terraza", "Patio"
]

for ambiente in Casa:
    nodo = {
        'value': ambiente,
        'aristas': []
        }
    grafo.insert_vertice(ambiente)


# Cocina - Aristas 3
grafo.insert_arista('Cocina', 'Comedor', 2)
grafo.insert_arista('Cocina', 'Sala de estar', 4)
grafo.insert_arista('Cocina', 'Patio', 3)

# Comedor - Aristas 5
grafo.insert_arista('Comedor', 'Habitación 1', 3)
grafo.insert_arista('Comedor', 'Habitación 2', 3)

# Habitación 1 - Aristas 4
grafo.insert_arista('Habitación 1', 'Habitación 2', 1)
grafo.insert_arista('Habitación 1', 'Baño 1', 1)

# Habitación 2 - Aristas 4
grafo.insert_arista('Habitación 2', 'Terraza', 3)
grafo.insert_arista('Habitación 2', 'Baño 2', 1)

# Baño 1 - Aristas 4
grafo.insert_arista('Baño 1', 'Cochera', 1)
grafo.insert_arista('Baño 1', 'Sala de estar', 2)

# Baño 2 - Aristas 4
grafo.insert_arista('Baño 2', 'Terraza', 1)
grafo.insert_arista('Baño 2', 'Patio', 5)

# Sala de estar - Aristas 5
grafo.insert_arista('Sala de estar', 'Comedor', 2)
grafo.insert_arista('Sala de estar', 'Baño 2', 1)

# Terraza - Aristas 3
grafo.insert_arista('Terraza', 'Habitación 1', 3)

# Cochera - Aristas 4
grafo.insert_arista('Cochera', 'Comedor', 2)
grafo.insert_arista('Cochera', 'Sala de estar', 3)

# Patio - Aristas 3
grafo.insert_arista('Patio', 'Quincho', 2)
grafo.insert_arista('Patio', 'Sala  de estar', 4)

# Quincho - Aristas 3
grafo.insert_arista('Quincho', 'Cochera', 1)
grafo.insert_arista('Quincho', 'Baño 1', 5)

grafo.show_graph()


# c
print()
grafo.mark_as_not_visited()
arbol_expansion = grafo.kruskal('Baño 2')
print(arbol_expansion)
print()
c = 0
for arista in arbol_expansion[0].split(';'):
    origen, destino, peso = arista.split('-')
    c += int(peso)
    print(f"Origen: {origen} -> Destino: {destino} Peso: {peso}")
print()
print(f"Se necesitan {c} metros de cable para conectar todos los ambientes")


# d
print()
grafo.mark_as_not_visited()
camino = grafo.dijkstra('Habitación 1')
destino = 'Sala de estar'
peso_total = None
camino_completo = []
while camino.size() > 0:
    value = camino.pop()
    if value[1][0] == destino:
        if peso_total is None:
            peso_total = value[0]
        camino_completo.append(value[1][0])
        destino = value[1][2]
camino_completo.reverse()
print(f"El camino mas corto es: {' - '.join(camino_completo)}, se necesitan {peso_total} metros de cable")

