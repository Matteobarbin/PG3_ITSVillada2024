def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        division = num1 / num2
        print(f"La división de {num1} respecto a {num2} es: {division}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

if __name__ == "__main__":
    main()
