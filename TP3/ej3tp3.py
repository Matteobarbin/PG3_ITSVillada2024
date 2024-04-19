def obtener_nombre_mes(numero_mes):
    meses_del_ano = ("enero", "febrero", "marzo", "abril", "mayo", "junio",
                     "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    try:
        nombre_mes = meses_del_ano[numero_mes - 1]
        print("El nombre del mes es:", nombre_mes)
    except IndexError:
        print("Número de mes fuera de rango.")

if __name__ == "__main__":
    try:
        numero_mes = int(input("Ingrese el número de mes (1-12): "))
        obtener_nombre_mes(numero_mes)
    except ValueError:
        print("Error: Por favor ingrese un número válido.")
