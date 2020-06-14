import json
from market.models import Genre

with open('generos.json', 'r') as fp:
    generos = json.load(fp)

for g in generos:
    n = Genre(name=g['name'])
    n.save()
    print('GUARDADO: ' + n.name)