def encontrar_mayor_menor(lista):
    if not lista:
        return None, None
    mayor = lista[0]
    menor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    return mayor, menor

entrada = input("Introduce números separados por espacios: ")
numeros = [float(x) for x in entrada.split()]

maximo, minimo = encontrar_mayor_menor(numeros)
print(f"El número mayor es: {maximo}")
print(f"El número menor es: {minimo}")
