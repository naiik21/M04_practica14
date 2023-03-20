"""
Declaramos una obj llamado school con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""

class school:
    def __init__(self, nombre, ciudad, pais, nEstudiantes, especializacion, nPlantas):
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.nEstudiantes = nEstudiantes
        self.especializacion = especializacion
        self.nPlantas = nPlantas

    def getnombre(self):
        return self.nombre

    def setnombre(self, nombre):
        self.nombre = nombre

    def getciudad(self):
        return self.ciudad

    def setciudad(self, ciudad):
        self.ciudad = ciudad

    def getpais(self):
        return self.pais

    def setpais(self, pais):
        self.pais = pais

    def getnEstudiantes(self):
        return self.nEstudiantes

    def setnEstudiantes(self, nEstudiantes):
        self.nEstudiantes = nEstudiantes

    def getespecializacion(self):
        return self.especializacion

    def setespecializacion(self, especializacion):
        self.especializacion = especializacion

    def getnPlantas(self):
        return self.nPlantas

    def setnPlantas(self, nPlantas):
        self.nPlantas = nPlantas

    def info(self):
        print("El nombre de la escuela es: " + self.nombre)
        print("La ciudad donde esta situada es: " + self.ciudad)
        print("Y el pais: " + self.pais)
        print("El numero de estudiantes es: " + self.nEstudiantes)
        print("La escuela se especializa en: " + self.especializacion)
        print("Y la escuela tiene: " + self.nPlantas + " plantas" + ".\n")

    def to_dict(self):
        return{
            "nombre": self.nombre,
            "ciudad": self.ciudad,
            "pais": self.pais,
            "nEstudiantes": self.nEstudiantes,
            "especializacion": self.especializacion,
            "nPlantas": self.nPlantas
        }