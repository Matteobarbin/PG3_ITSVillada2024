class Familia:
    def __init__(self):
        self.padre = input("Padre: ")
        self.madre = input("Madre: ")
        self.hijos = ["Juan","Valentin","Juana"]

    def __str__(self):
        return f" Padre:{self.padre}, Madre:{self.madre}, Hijos:{self.hijos}"
    

print(Familia())