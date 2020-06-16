import json
from market.models import Book, Author, Editorial, Genre
from random import randrange

#import .cargar_autores, .cargar_editoriales, .cargar_generos, .cargar_paises

# Selecciono Autor, Editorial y Género de manera aleatoria
with open('autores.json', 'r') as fp:
    autores = json.load(fp)
with open('editoriales.json', 'r') as fp:
    editoriales = json.load(fp)
with open('generos.json', 'r') as fp:
    generos = json.load(fp)
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
    print('GUARDADO: ' + n)