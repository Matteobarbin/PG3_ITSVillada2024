def contar_vocales(frase):
    
    contador_vocales = 0
   
    vocales = "aeiouAEIOU"
    
    for caracter in frase:
    
        if caracter in vocales:
            contador_vocales += 1
   
    return contador_vocales


frase = input("Ingresa una frase: ")
cantidad_vocales = contar_vocales(frase)
print("La cantidad de vocales en la frase es:", cantidad_vocales)
