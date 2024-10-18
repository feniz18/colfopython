from clases.animal import Animal, Llamar

class Gato(Animal, Llamar):
    def __init__(self,nombre):
        super().__init__(nombre,4)


gato1 = Gato('Polar')

gato1.saludar()

gato1.saludar()