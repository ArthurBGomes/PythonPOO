from abc import ABC,abstractmethod
import math
class Poligono(ABC):
    def __init__(self,qntd_lados):
        self.qtnd_lados = qntd_lados
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Quadrado(Poligono):
    def __init__(self,lado):
        self.lado = lado
    def perimetro(self):
        return self.lado * 4
    def area(self):
        return self.lado**2
class Circulo(Poligono):
    def __init__(self,raio):
        self.raio = raio
    def perimetro(self):
        return self.raio * 2 * math.pi
    def area(self):
        return math.pi * self.raio**2