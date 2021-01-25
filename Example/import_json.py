import json

data = {}
data['Persona'] = []

data['Persona'].append({
    'Id': 1,
    'name': 'admin Deportivo',
    'email': 'admin@gmail.com',
    'cel': 8711001100,
    'prestamos': 3
    })

data['Persona'].append({
    'Id': 2,
    'name': 'Nestor Puentes',
    'email': 'nestor@gmail.com',
    'cel': 8711111100,
    'prestamos': 3
    })

with open('dataPersonas.json', 'w') as file:
    json.dump(data, file, indent=4)

#https://www.analyticslane.com/2018/07/16/archivos-json-con-python/
#https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=100&codigo=101&inicio=90