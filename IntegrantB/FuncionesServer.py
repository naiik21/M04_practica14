import requests


def showJson(object):
    dat= []
    for i in object.json():
        data.append(i)

    return data


def newCat(newLineCat):
    requests.post('https//loclahost:3000/cat', data=newLineCat)

def newBook(newLineBook):
    requests.post('https//loclahost:3000/book', data=newLineBook)


def deletCat(id)
    requests.delete('https//loclahost:3000/cat' + str(id))


def deletBook(id)
    requests.delete('https//loclahost:3000/book' + str(id))


