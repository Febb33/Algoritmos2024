
class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero         
        self.nombre = nombre         
        self.tipos = tipos           
        self.nivel = nivel           

def agregar_pokemon(pokemon):

    for tipo in pokemon.tipos:
        if tipo not in hash_tipo:
            hash_tipo[tipo] = []
        hash_tipo[tipo].append(pokemon)

    ultimo_digito = pokemon.numero % 10
    hash_digito[ultimo_digito].append(pokemon)

    nivel_index = pokemon.nivel // 10
    if nivel_index < 10:  
        hash_nivel[nivel_index].append(pokemon)

def digitos():
    for i in range(10):
        for pokemon in hash_digito[i]:
            if i in [3, 7, 9]:
                print(f"   {pokemon.nombre}")

def multiplos():
    for nivel_lista in hash_nivel:
        for pokemon in nivel_lista:
            if pokemon.nivel % 2 == 0 or pokemon.nivel % 5 == 0 or pokemon.nivel % 10 == 0:
                print(f"   {pokemon.nombre}")

def tipos_espe(tipos):
    for tipo in tipos:
        if tipo in hash_tipo:
            for pokemon in hash_tipo[tipo]:
                print(f"   {pokemon.nombre}")


hash_tipo = {}     
hash_digito = [[] for _ in range(10)]  
hash_nivel = [[] for _ in range(10)]    


agregar_pokemon (Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], 5))
agregar_pokemon (Pokemon(71, "Ivysaur", ["Planta", "Veneno"], 15))
agregar_pokemon (Pokemon(3, "Charmander", ["Fuego"], 9))
agregar_pokemon(Pokemon(103, "Exeggutor", ["Planta", "Psíquico"], 35))
agregar_pokemon (Pokemon(3, "Squirtle", ["Agua"], 10))
agregar_pokemon (Pokemon(7, "Pidgey", ["Normal", "Volador"], 13))
agregar_pokemon (Pokemon(2, "Steelix", ["Acero", "Tierra"], 30))
agregar_pokemon (Pokemon(87, "Gengar",["Fantasma", "Veneno"],90))
agregar_pokemon (Pokemon(59, "Electabuzz",["Electrifico"],14))
agregar_pokemon (Pokemon(27, "Mamoswine",["Hielo", "Tierra"],13))
agregar_pokemon(Pokemon(25, "Pikachu", ["Electrico"], 12))
agregar_pokemon(Pokemon(6, "Charizard", ["Fuego", "Volador"], 36))
agregar_pokemon(Pokemon(130, "Gyarados", ["Agua", "Volador"], 55))
agregar_pokemon(Pokemon(131, "Lapras", ["Agua", "Hielo"], 30))
agregar_pokemon(Pokemon(9, "Blastoise", ["Agua"], 50))


print()
print("Pokémons cuyos números terminan en 3, 7 y 9:")
digitos()


print()
print("Pokémons con niveles múltiplos de 2, 5 y 10:")
multiplos()


print()
print("Pokémons de tipos : Acero, Fuego, Electrifico y Hielo:")
tipos_espe(["Acero", "Fuego", "Electrifico", "Hielo"])

