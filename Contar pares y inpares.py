def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

entrada = input("Introduce números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]

total_pares, total_impares = contar_pares_impares(numeros)
print(f"Cantidad de pares: {total_pares}")
print(f"Cantidad de impares: {total_impares}")
