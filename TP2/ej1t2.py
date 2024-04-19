class Persona:

    def __init__(self) :
        self.nombre = input("Ingrese su nombre: ")

  
    def imprimir(self):
        print(f"{self.nombre} \n bienvenido")


persona1=Persona()
persona1.imprimir()