import requests
from IntegrantB.FuncionesServer import *


catObj= requests.get('https//loclahost:3000/cat')
bookObj= requests.get('https//loclahost:3000/book')
infoCat= showJson(catObj)
infoBook= showJson(bookObj)

# Declaramos nueevos obj
newLinesCat= {'nom':'Meow','color':'negro', 'id':'6','nomAmo':'Pedro','raza':'Gato','mida':'Grande','sexo':'Macho' }
newLinesBook= {'nom':'BatPad','autor':'Anonimo', 'id':'6','portada':'blanda','pagines':'173','categoria':'Aventura','editorial':'Estrella polar' }

#Los añadimos al json
newCat(newLinesCat)
newBook(newLinesBook)

# Borramos obj del json
deletCat(6)
deletBook(6)

