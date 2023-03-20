"""
Declaramos una obj llamado vehicle con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""

class car:
    def __init__(self, marca, modelo, año, pais):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.pais = pais

    def getmarca(self):
        return self.marca

    def setmarca(self, marca):
        self.marca = marca

    def getmodelo(self):
        return self.modelo

    def setmodelo(self, modelo):
        self.modelo = modelo

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        self.color = color

    def getaño(self):
        return self.año

    def setaño(self, año):
        self.año = año

    def salutació(self):
        print("La marca es: " + self.marca)
        print("El modelo: " + self.modelo)
        print("El año de fabricación del coche es: " + self.año)
        print("El pais de fabricación: " + self.pais + ".\n")

    def to_dict(self):
        return{
            "marca": self.marca,
            "modelo": self.modelo,
            "pais": self.pais,
            "año": self.año
        }