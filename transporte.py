class Transporte:
    def __init__(self, ruedas:int, asientos:int) -> None:
        self.ruedas = ruedas
        self.asientos = asientos

    def desplazar(self, x:int, y:int):
        print(f"Moviendose a x: {x} metros y: {y} metros")

    def informacion(self):
        print(f"ruedas: {self.ruedas} asientos: {self.asientos}")