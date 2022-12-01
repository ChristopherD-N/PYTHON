class Vehículo:
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    
class Coche(Vehículo):
    velocidad = None
    cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        
        super().__init__(color, ruedas, puertas)
        
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        

seat = Coche("gris", 16.5, 4, 120, 1.9)
print(seat.color, seat.ruedas, seat.puertas, seat.velocidad, seat.cilindrada)
