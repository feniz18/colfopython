#Diccionarios en python simples.

lista = [
    {
    'nombre': 'David',
    'apellido': 'Martinez',
    'edad': 30,
    'fechaNacimiento': '30/07/1994',
    'telefono': [
        '3185551972',
        '3146651234'
    ]
    },
    {
    'nombre': 'Billy',
    'apellido': 'Lozano',
    'edad': 30,
    'fechaNacimiento': '30/07/1994',
    'telefono': [
        '3185551972',
        '3146651234'
    ]
    },
    {
    'nombre': 'Alexandra',
    'apellido': 'Correa',
    'edad': 30,
    'fechaNacimiento': '30/07/1994',
    'telefono': [
        '3185551972',
        '3146651234'
    ]
    },
]

#Ciclo for

for i in lista:
    print(i['nombre'])
    for j in i['telefono']:
        print(j)

