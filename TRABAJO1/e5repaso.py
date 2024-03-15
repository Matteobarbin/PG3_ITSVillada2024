
def esPalindromo(palabra):
   
    if palabra == palabra[::-1]:
        print("true")
    else:
        print("false")


palabra_analizada = input("ingresa la palabra que quieres analizar: ")


esPalindromo(palabra_analizada)