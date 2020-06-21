import json
from market.models import Discount

with open('descuentos.json', 'r') as fp:
    descuentos = json.load(fp)

for d in descuentos:
    n = Discount(value=d['value'])
    n.save()
    print('GUARDADO: ', n)