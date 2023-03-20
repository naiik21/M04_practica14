import json

from IntegrantB.book import book
from IntegrantB.cat import cat
from IntegrantA.car import car
from IntegrantA.school import school


books = [
    book("El señor de los anillos", "J.r.r. Tolkien","1", "dura", "488", "Novela Fantastica", "MINOTAURO"),
    book("El cuco de cristal", "Javier Castillo","2", "blanda", "488", "Novela", "SUMA"),
    book("TODO LO QUE NUNCA TE DIJE", "Sara Herranz","3", "dura", "176", "Novela", "SUMA"),
    book("Así es la puta vida", "Jordi Wild","4", "dura", "300", "ANTI-autoayuda", "Plan B"),
    book("Kimetsu no yaiba 2", "Koyoharu Gotouge","5", "blanda", "192", "Manga", "Norma Editorial")
]

cats = [
    cat("Gato", "Marron","1", "Javier", "Abisinio", "Grande", "Macho"),
    cat("Misha", "Balnco","2", "Raul", "Asiático", "Pequeño", "Hembra"),
    cat("Tom", "Negro","3", "Joan", "Balinés", "Grande", "Macho"),
    cat("Luigi", "Marron","4", "Ferran", "Balinés", "Pequeño", "Macho"),
    cat("Tutancamon", "Carne","5", "Fran", "Egipcio", "Pequeño", "Hembra")
]

books_list= [b.to_dict() for b in books]

cats_list= [c.to_dict() for c in cats]

data = {"books":books_list, "cats":cats_list}

with open("jsonAPI/data.json", 'w') as file:
    json.dump(data, file)


