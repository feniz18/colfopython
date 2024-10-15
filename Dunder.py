#Los metodos dunder sirven para manipular la clase y vienen incluidos en la 
#Estructura de datos de los Objetos Python

class Afiliado:
    nombre = ''
    calificacion = 0
    edad = 0

    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def getCalificacion(self):
        calificacion = f"tu calificación es {self.calificacion}"
        return calificacion
    
    def setCalificacion(self,calificacion):
        self.calificacion = int(calificacion) + 1
    
daniel = Afiliado('Daniel',18)

daniel.setCalificacion(5)

calificacionDaniel = daniel.getCalificacion()

print(daniel)