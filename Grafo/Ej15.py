
from Grafo import Graph

grafo = Graph(dirigido = False)

Maravillas = [
    {
        "nombre": "Chichén Itzá",
        "pais": "México",
        "tipo": "Arquitectónica"
    },
    {
        "nombre": "Coliseo de Roma",
        "pais": "Italia",
        "tipo": "Arquitectónica"
    },
    {
        "nombre": "Cristo Redentor",
        "pais": "Brasil",
        "tipo": "Arquitectónica"
    }, 
    {
        "nombre": "Gran Muralla China",
        "pais": "China",
        "tipo": "Arquitectónica"
    },
    {
        "nombre": "Machu Picchu",
        "pais": "Perú",
        "tipo": "Arquitectónica"
    },
    {
        "nombre": "Taj Mahal",
        "pais": "India",
        "tipo": "Arquitectónica"
    },
    {
        "nombre": "Petra",
        "pais": "Jordania",
        "tipo": "Arquitectónica"
    },
    # Maravillas Naturales
    {
        "nombre": "Cataratas del Iguazú",
        "pais": "Argentina/Brasil",
        "tipo": "Natural"
    },
    {
        "nombre": "Isla de Jeju",
        "pais": "Corea del Sur",
        "tipo": "Natural"
    },
    {
        "nombre": "Río Subterráneo Puerto Princesa",
        "pais": "Filipinas",
        "tipo": "Natural"
    },
    {
        "nombre": "Isla de Komodo",
        "pais": "Indonesia",
        "tipo": "Natural"
    },
    {
        "nombre": "Montaña de la Mesa",
        "pais": "Sudáfrica",
        "tipo": "Natural"
    },
    {
        "nombre": "Bahía Ha Long",
        "pais": "Vietnam",
        "tipo": "Natural"
    },
    {
        "nombre": "Amazonia",
        "pais": "Bolivia/Brasil/Colombia/Ecuador/Guayana Francesa/Guyana/Perú/Surinam/Venezuela",
        "tipo": "Natural"
    }
]


for Maravilla in Maravillas:
    nodo = {
        'value': Maravilla["nombre"],
        'other_value': Maravilla,
        'aristas': []
        }
    grafo.insert_vertice_2(Maravilla["nombre"], Maravilla)


# Maravillas Arquitectónicas
grafo.insert_arista("Chichén Itzá", "Coliseo de Roma", 3000)
grafo.insert_arista("Cristo Redentor", "Petra", 5000)
grafo.insert_arista("Gran Muralla China", "Machu Picchu", 9000)
grafo.insert_arista("Gran Muralla China", "Coliseo de Roma", 7000)
grafo.insert_arista("Chichén Itzá", "Cristo Redentor", 8000)
grafo.insert_arista("Taj Mahal", "Petra", 16000)
grafo.insert_arista("Petra", "Chichén Itzá", 20000)
grafo.insert_arista("Gran Muralla China", "Chichén Itzá", 18000)
grafo.insert_arista("Machu Picchu", "Taj Mahal", 3000)
grafo.insert_arista("Chichén Itzá", "Taj Mahal", 8000)
grafo.insert_arista("Machu Picchu", "Chichén Itzá", 1000)
grafo.insert_arista("Gran Muralla China", "Petra", 5000)
grafo.insert_arista("Taj Mahal", "Gran Muralla China", 6000)
grafo.insert_arista("Cristo Redentor", "Gran Muralla China", 21000)
grafo.insert_arista("Coliseo de Roma", "Petra", 2000)
grafo.insert_arista("Machu Picchu", "Petra", 24000)
grafo.insert_arista("Coliseo de Roma", "Taj Mahal", 5000)
grafo.insert_arista("Taj Mahal", "Cristo Redentor", 8000)
grafo.insert_arista("Cristo Redentor", "Coliseo de Roma", 26000)
grafo.insert_arista("Coliseo de Roma", "Machu Picchu", 11000)
grafo.insert_arista("Machu Picchu", "Cristo Redentor", 10000)
# Maravillas Naturales
grafo.insert_arista("Cataratas del Iguazú", "Isla de Jeju", 60100)
grafo.insert_arista("Isla de Komodo", "Río Subterráneo Puerto Princesa", 4100)
grafo.insert_arista("Isla de Jeju", "Amazonia", 5200)
grafo.insert_arista("Montaña de la Mesa", "Bahía Ha Long", 1200)
grafo.insert_arista("Río Subterráneo Puerto Princesa", "Amazonia", 5800)
grafo.insert_arista("Amazonia", "Bahía Ha Long", 9700)
grafo.insert_arista("Río Subterráneo Puerto Princesa", "Bahía Ha Long", 3200)
grafo.insert_arista("Isla de Komodo", "Montaña de la Mesa", 18000)
grafo.insert_arista("Amazonia", "Cataratas del Iguazú", 9300)
grafo.insert_arista("Cataratas del Iguazú", "Bahía Ha Long", 6700)
grafo.insert_arista("Río Subterráneo Puerto Princesa", "Isla de Jeju", 23500)
grafo.insert_arista("Bahía Ha Long", "Isla de Komodo", 5000)
grafo.insert_arista("Isla de Komodo", "Cataratas del Iguazú", 1600)
grafo.insert_arista("Isla de Jeju", "Isla de Komodo", 21000)
grafo.insert_arista("Cataratas del Iguazú", "Río Subterráneo Puerto Princesa", 1000)
grafo.insert_arista("Bahía Ha Long", "Isla de Jeju", 24000)
grafo.insert_arista("Cataratas del Iguazú", "Montaña de la Mesa", 2500)
grafo.insert_arista("Amazonia", "Isla de Komodo", 8000)
grafo.insert_arista("Montaña de la Mesa", "Río Subterráneo Puerto Princesa", 32000)
grafo.insert_arista("Amazonia", "Montaña de la Mesa", 2000)
grafo.insert_arista("Montaña de la Mesa", "Isla de Jeju", 5000)


grafo.show_graph()


# c
print()
grafo.mark_as_not_visited()
arbol_expansion = grafo.kruskal('')
print('Árbol expansión mínima:')
print(arbol_expansion)
print()
for arista in arbol_expansion[0].split(';'):
    origen, destino, peso = arista.split('-')
    print(f"Origen: {origen} -> Destino: {destino} / Distancia: {peso}")
print()

# No supe hacer el arbol de expansion por tipos


# d
# Este punto tampoco


