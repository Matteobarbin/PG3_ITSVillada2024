def anio_bisiesto(anio) :
    if (anio%4 == 0 and anio%100 != 0) or (anio%400):
        print("el año es bisiesto")
    else:
        print("el año no es bisiesto")


anio = int(input("ingrese el elemento a buscar"))

anio_bisiesto(anio)