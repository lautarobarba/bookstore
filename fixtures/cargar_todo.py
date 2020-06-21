import json
from users.models import Country
from market.models import Author, Discount, Editorial, Genre, Book
from random import randrange

#Cargar Paises
print('CARGANDO PAISES')
with open('paises.json', 'r') as fp:
    paises = json.load(fp)

for p in paises:
    n = Country(name=p['name'])
    n.save()
    print('GUARDADO: ' + n.name)

#Cargar Autores
print('CARGANDO AUTORES')
with open('autores.json', 'r') as fp:
    autores = json.load(fp)

for a in autores:
    n = Author(first_name=a['first_name'], last_name=a['last_name'])
    n.save()
    print('GUARDADO: ' + n.first_name + ' ' + n.last_name)

#Cargar Descuentos
print('CARGANDO DESCUENTOS')
with open('descuentos.json', 'r') as fp:
    descuentos = json.load(fp)

for d in descuentos:
    n = Discount(value=d['value'])
    n.save()
    print('GUARDADO: ', n)

#Cargar editoriales
print('CARGANDO EDITORIALES')
with open('editoriales.json', 'r') as fp:
    editoriales = json.load(fp)

for e in editoriales:
    n = Editorial(name=e['name'])
    n.save()
    print('GUARDADO: ' + n.name)

#Cargar Generos
print('CARGANDO GENEROS')
with open('generos.json', 'r') as fp:
    generos = json.load(fp)

for g in generos:
    n = Genre(name=g['name'])
    n.save()
    print('GUARDADO: ' + n.name)

#Cargar Libros
print('CARGANDO LIBROS')
with open('libros.json', 'r') as fp:
    libros = json.load(fp)

for l in libros:
    #Seleccion aleatoria
    a = autores[randrange(len(autores))]
    autor_random = Author.objects.get(first_name__icontains=a['first_name'], last_name__icontains=a['last_name'])
    e = editoriales[randrange(len(editoriales))]
    editorial_random = Editorial.objects.get(name__icontains=e['name'])
    g = generos[randrange(len(generos))]
    genero_random = Genre.objects.get(name__icontains=g['name'])
    
    #Cargo los datos del libro y lo guardo
    n = Book(title=l['title'], isbn=l['isbn'], sinopsis=l['sinopsis'], price=l['price'], editorial=editorial_random)
    n.save()
    #Necesita una id para crear la relación, por eso lo guarde antes
    n.authors.add(autor_random)
    n.genres.add(genero_random)
    print('GUARDADO: ' + n.title)