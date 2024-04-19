try:
    with open("archivo.txt", "w") as archivo:
        # Intentamos escribir una serie de strings en el archivo
        archivo.write("Hola\n")
        archivo.write("Este es un ejemplo\n")
        archivo.write("de almacenamiento\n")
        archivo.write("de strings en un archivo de texto.\n")
        
        # Intentamos llamar al método 'write' pasando un entero
        archivo.write(42)  # Esto generará un TypeError
except TypeError as e:
    print("Error: Se ha producido un error de tipo:", e)
