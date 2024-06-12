
nombres = ["Pedro", "Mario", "Sebastian", "Juan", "Lucas", "Walter"]

def inverso(lista):
    if len(lista) == 1:
        print(lista [0])
    else:
        print(lista[-1])
        inverso(lista[:-1])

print()
inverso(nombres)
