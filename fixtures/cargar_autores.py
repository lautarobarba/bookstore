import json
from market.models import Author

with open('autores.json', 'r') as fp:
    autores = json.load(fp)

for a in autores:
    n = Author(first_name=a['first_name'], last_name=a['last_name'])
    n.save()
    print('GUARDADO: ' + n.first_name + ' ' + n.last_name)