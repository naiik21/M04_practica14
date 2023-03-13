"""
Declaramos una obj llamado cat con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""
class cat:
    def __init__(self, nom, color, nomAmo, raza, mida, sexo):
        self.nom= nom
        self.color = color
        self.nomAmo = nomAmo
        self.raza = raza
        self.mida = mida
        self.sexo = sexo

    def getnom(self):
        return self.nom

    def setnom(self, nom):
        self.nom = nom

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        self.color = color

    def getnomAmo(self):
        return self.nomAmo

    def setnomAmo(self, nomAmo):
        self.nomAmo = nomAmo

    def getraza(self):
        return self.raza

    def setraza(self, raza):
        self.raza = raza

    def getmida(self):
        return self.mida

    def setmida(self, mida):
        self.mida = mida

    def getsexo(self):
        return self.sexo

    def setsexo(self, sexo):
        self.sexo = sexo


    def info(self):
        print("El nom del gat es: " + self.nom)
        print("es de color " + self.color)
        print("es de mida " + self.mida + ", ")
        print("de raza " + self.raza + " i ")
        print(self.sexo + ".")
        print("El seu amo es diu " + self.nomAmo + ".\n")

    def to_dict(self):
        return {
            "nom":self.nom,
            "color": self.color,
            "nomAmo": self.nomAmo,
            "raza": self.raza,
            "mida": self.mida,
            "sexo": self.sexo
        }