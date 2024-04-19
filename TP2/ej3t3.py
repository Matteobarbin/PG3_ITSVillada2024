class Triangulo:
    def __init__(self):
        self.lado1 = float(input("Ingrese la longitud del primer lado: "))
        self.lado2 = float(input("Ingrese la longitud del segundo lado: "))
        self.lado3 = float(input("Ingrese la longitud del tercer lado: "))
        self.imprimir_lado_mayor()
        self.es_equilatero()
    def imprimir_lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado mayor es:", mayor)
    
    def es_equilatero(self):
        if (self.lado1 == self.lado2 == self.lado3):
            print("El triángulo es equilátero.")
    
        else:
            print("El triángulo no es equilátero.")

            
       




triangulo1= Triangulo()

triangulo1.__init__

