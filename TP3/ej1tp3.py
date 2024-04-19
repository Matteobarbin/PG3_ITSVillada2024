def obtener_entero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un valor entero válido.")

def main():
    while True:
        try:
            num1 = obtener_entero()
            num2 = obtener_entero()
            suma = num1 + num2
            print(f"La suma de {num1} y {num2} es: {suma}")

            continuar = input("¿Desea seguir sumando valores? (s/n): ")
            if continuar.lower() != 's':
                break
        except Exception as e:
            print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    main()
