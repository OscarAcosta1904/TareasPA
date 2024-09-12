class Circulo:
    radio = 0
    
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self): 
        self.area = self.radio*3.1416*self.radio
        print("\narea del circulo: ", self.area)
        
        
    def calcular_perimetro(self):
        self.perimetro = 2*self.radio*3.1416
        print("\ndiametro del circulo: ", self.perimetro)