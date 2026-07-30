def sumar_elementos(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

entrada = input("Introduce números separados por espacios: ")
numeros = [float(x) for x in entrada.split()]

resultado = sumar_elementos(numeros)
print(f"La suma total es: {resultado}")
