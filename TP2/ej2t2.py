class Alumno :
    def __init__(self):
        self.nombre =input("nombre: ")
        self.nota =int(input("nota: "))
        self.mostrar_datos()
        self.cargar_estado()

    def mostrar_datos(self):
        print(f"\n nombre:{self.nombre}\n nota: {self.nota} ")
    
    def cargar_estado(self):
        if (self.nota>=4):
            print("es un algumno regular")
        else :
            print("es un alumno libre")



Alumno1=Alumno()
Alumnto2=Alumno()