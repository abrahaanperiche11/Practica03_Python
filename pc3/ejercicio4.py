class Rectangulo:
    
    #método de inicialización
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    #definimos método para calcular el área:
    def area_rectangulo(self):
        return self.ancho * self.largo

#ejemplo
if __name__=='__main__':
    rectangulo_1=Rectangulo(2,3)
    print(rectangulo_1.area_rectangulo())