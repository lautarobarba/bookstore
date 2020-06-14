import json
from users.models import Country

with open('paises.json', 'r') as fp:
    paises = json.load(fp)

for p in paises:
    n = Country(name=p['name'])
    n.save()
    print('GUARDADO: ' + n.name)