"""
Declaramos una obj llamado book con sus 6 atributos ,
sus correspondientes getters y setters
y una funcion que nos devuelve su info
"""
class book:
    def __init__(self, nom, autor, id, portada, pagines, categoria, editorial):
        self.nom= nom
        self.autor = autor
        self.id= id
        self.portada = portada
        self.pagines = pagines
        self.categoria = categoria
        self.editorial = editorial

    def getnom(self):
        return self.nom

    def setnom(self, nom):
        self.nom = nom

    def getautor(self):
        return self.autor

    def setautor(self, autor):
        self.autor = autor

    def getid(self):
        return self.id

    def setid(self, id):
        self.id = id

    def getportada(self):
        return self.portada

    def setportada(self, portada):
        self.portada = portada

    def getpagines(self):
        return self.pagines

    def setpagines(self, pagines):
        self.pagines = pagines

    def getcategoria(self):
        return self.categoria

    def setcategoria(self, categoria):
        self.categoria = categoria

    def geteditorial(self):
        return self.editorial

    def seteditorial(self, editorial):
        self.editorial = editorial


    def info(self):
        print("El nom del llibre es: " + self.nom)
        print("El seu auto es, " + self.autor + ", ")
        print("te una portada " + self.portada)
        print("un total de " + self.pagines + " pagines,")
        print("la seva categoria es " + self.categoria + " i ")
        print("la editorial " + self.editorial + ".\n")

    def to_dict(self):
        return {
            "nom":self.nom,
            "autor": self.autor,
            "id": self.id,
            "portada": self.portada,
            "pagines": self.pagines,
            "categoria": self.categoria,
            "editorial": self.editorial
        }