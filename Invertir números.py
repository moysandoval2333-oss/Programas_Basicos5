def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

entrada = input("Introduce elementos separados por espacios: ")
elementos = entrada.split()

resultado = invertir_lista(elementos)
print(f"Lista invertida: {resultado}")
