def areaCirculo(radio):
    pi = 3.1416
    area = pi * (radio**2)
    return area

def volumenCilindro(altura, radio):
    areaCilindro = areaCirculo(radio)
    volumenCilindro = areaCilindro * altura
    return volumenCilindro


cilindro = volumenCilindro(10,5)

print(cilindro)