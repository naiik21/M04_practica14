import json

from IntegrantB.book import book
from IntegrantB.cat import cat

books = [
    book("El señor de los anillos", "J.r.r. Tolkien", "dura", "488", "Novela Fantastica", "MINOTAURO"),
    book("El cuco de cristal", "Javier Castillo", "blanda", "488", "Novela", "SUMA"),
    book("TODO LO QUE NUNCA TE DIJE", "Sara Herranz", "dura", "176", "Novela", "SUMA"),
    book("Así es la puta vida", "Jordi Wild", "dura", "300", "ANTI-autoayuda", "Plan B"),
    book("Kimetsu no yaiba 2", "Koyoharu Gotouge", "blanda", "192", "Manga", "Norma Editorial")
]

cats = [
    cat("Gato", "Marron", "Javier", "Abisinio", "Grande", "Macho"),
    cat("Misha", "Balnco", "Raul", "Asiático", "Pequeño", "Hembra"),
    cat("Tom", "Negro", "Joan", "Balinés", "Grande", "Macho"),
    cat("Luigi", "Marron", "Ferran", "Balinés", "Pequeño", "Macho"),
    cat("Tutancamon", "Carne", "Fran", "Egipcio", "Pequeño", "Hembra")
]

books_list= [b.to_dict() for b in books]

cats_list= [c.to_dict() for c in cats]

data = {"books":books_list, "cats":cats_list}

with open("jsonAPI/data.json", 'w') as file:
    json.dump(data, file)