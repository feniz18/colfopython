#Tuplas y listas 

#Tuplas: No son modificables= Inmutables
#listas: Permiten modificar los datos originas: Mutables

#tuplas caracteristica ()

tupla = ('David', 'Billy', 'Adriana', 'Daniel','Adriana')


#listas

lista = ['David', 'Billy', 'Adriana', 'Daniel','Adriana']
lista2 = ['Milton', 'JOse']
lista.extend(lista2)
lista.pop()

lista2d = [
    [
        'David',
        'Martinez',
        '30',
        '30/07/2024'
    ],
    [
        'Adriana',
        'Romero',
        '--',
        '30/07/20--'
    ],
    [
        'Billy',
        'Lozano',
        '--',
        '30/07/20--'
    ]
]

#print(lista[0])

print(lista2d[2][3])