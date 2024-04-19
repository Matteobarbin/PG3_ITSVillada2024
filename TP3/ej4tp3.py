def realizar_division():
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        
        resultado = numero1 / numero2
        print("El resultado de la división es:", resultado)
        
    except ValueError:
        print("Error: Por favor ingrese solo números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

if __name__ == "__main__":
    realizar_division()

