class Animal:
    nombre = ''
    patas = 0

    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.pata = patas
    
    def saludar(self):
        print('Hola soy' + self.nombre)

class Llamar:
    def llamar(self):
        print("Llamado desde clase secundaria de herencia")