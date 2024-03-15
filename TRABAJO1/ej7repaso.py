def es_numero_step(numero):
    
    num_str = str(numero)
    
    for i in range(len(num_str) - 1):
        digito_actual = int(num_str[i])
        siguiente_digito = int(num_str[i + 1])
        
        if abs(digito_actual - siguiente_digito) != 1:
            return False
            
    return True

def main():
    
    numero_usuario = input("Por favor, ingrese un número para verificar si es un número 'step': ")
    
    # Intentar convertir la entrada a un número entero y verificar si es un número "step"
    try:
        numero = int(numero_usuario)
        if es_numero_step(numero):
            print(f"¡El número {numero} es un número 'step'!")
        else:
            print(f"El número {numero} NO es un número 'step'.")
    except ValueError:
        # Manejar el error si la entrada no puede convertirse a un entero
        print("La entrada no es un número válido. Por favor, ingrese solo dígitos numéricos.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
