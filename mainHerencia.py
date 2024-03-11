from guagua import Guagua

def main():
    intercity = Guagua(6, 50)
    intercity.informacion()
    intercity.desplazar(10, 24)

    lanzaroteBus = Guagua(7, 30)
    lanzaroteBus.informacion()
    lanzaroteBus.desplazar(20, 5)

if __name__ == "__main__":
    main()