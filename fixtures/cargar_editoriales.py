import json
from market.models import Editorial

with open('editoriales.json', 'r') as fp:
    editoriales = json.load(fp)

for e in editoriales:
    n = Editorial(name=e['name'])
    n.save()
    print('GUARDADO: ' + n.name)