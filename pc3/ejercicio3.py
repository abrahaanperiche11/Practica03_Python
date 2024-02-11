import math
class Circulo:
    PI=math.pi
    
    def __init__( self, radio_circulo):
        self.radio = radio_circulo
        
    def area_circulo(self):
        return self.PI * (self.radio**2)
    
#ejemplo
if __name__=='__main__':
    circulo_1=Circulo(1)
    print(circulo_1.area_circulo())