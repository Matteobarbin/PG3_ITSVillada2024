def ordenar_de_mayor_a_menor(lista):
    n = len(lista)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if lista[j] > lista[max_index]:
                max_index = j
        lista[i], lista[max_index] = lista[max_index], lista[i]
    return lista


numeros_str = input("Ingresa los números separados por espacios: ")
numeros = [int(num) for num in numeros_str.split()]


lista_ordenada = ordenar_de_mayor_a_menor(numeros)


print("Lista original:", numeros_str)
print("Lista ordenada de mayor a menor:", lista_ordenada)
