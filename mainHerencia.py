from transporte import Transporte
from guagua import Guagua

def main():
    intercity = Guagua(4, 50)
    print(f"ruedas de intercity: {intercity.ruedas} asientos de intercity: {intercity.asientos}")
    intercity.desplazar(10, 24)

    lanzaroteBus = Guagua(7, 30)
    print(f"ruedas de intercity: {lanzaroteBus.ruedas} asientos de intercity: {lanzaroteBus.asientos}")
    lanzaroteBus.desplazar(20, 5)

if __name__ == "__main__":
    main()