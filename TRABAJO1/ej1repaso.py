def buscar_en_lista(lista, elemento):
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1  
mi_lista = [8, 12, 9, 45]
elemento_buscado = int(input("ingrese el elemento a buscar"))
indice_encontrado = buscar_en_lista(mi_lista, elemento_buscado)
if indice_encontrado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el índice {indice_encontrado}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")
