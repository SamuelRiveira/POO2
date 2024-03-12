class Vehiculo:
    def __init__(self, ruedas, color) -> None:
        self.ruedas = ruedas
        self.color = color
    def info(self):
        print(f"Ruedas: {self.ruedas} Color: {self.color}")
    