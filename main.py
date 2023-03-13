import json

from IntegrantB.book import book
from IntegrantB.cat import cat
from IntegrantA.car import car
from IntegrantA.school import school

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




cars = [
    car("Seat", "Ateca", "2022", "España"),
    car("Audi", "Q7", "2017", "Alemania"),
    car("BMW", "320d", "2018", "Alemania"),
    car("Ford", "Fiesta", "2023", "Estados Unidos"),
    car("Toyota", "RAV4", "2015", "Japon")
]

schools = [
    school("Jaume Balmes", "Barcelona", "España", "777", "Eso", "5"),
    school("La guineueta", "Barcelona", "España", "1778", "Bachillerato", "4"),
    school("Quatre Cantons", "Barcelona", "España", "582", "Eso", "3"),
    school("Xarau", "Cerdanyola del Valles", "España", "33", "Primaria", "2"),
    school("La Llacuna", "Barcelona", "España", "333", "Primaria", "4")
]

cars_list = [c.to_dict() for c in cars]

schools_list = [s.to_dict() for s in schools]

data = {"cars":cars_list, "schools":schools_list}

with open("jsonAPI/data1.json", "w") as file:
    json.dump(data, file)