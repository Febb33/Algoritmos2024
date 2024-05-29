
Mochila_jedi = ["agua caliente", "blaster", "mate", "alfajor", "sable de luz", "yerba"]

def Contador(vector, buscado, con):
    if con == len(vector):
        return -1
    elif vector[con] == buscado:
        return con+1
    else:
        con+=1
        return Contador(vector, buscado, con)

def Usar_la_fuerza(vector, buscado):
    if vector[0] == buscado:
        print("Encontraste el sable de luz, que la fuerza te acompañe")
    else:
        print("Sacaste:", vector[0])
        print()
        Usar_la_fuerza(vector[1:], buscado)

c = 0
buscado = "sable de luz"
x = Contador(Mochila_jedi, buscado, c)

if x == -1:
    print()
    print("No hay un sable de luz en tu mochila")
else:
    print()
    print("Encontraste el sable de luz en la posicion:", x)
print()
y = Usar_la_fuerza(Mochila_jedi, buscado)
