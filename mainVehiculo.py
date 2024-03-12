from automovil import Automovil
from bicicleta import Bicicleta
from camion import Camion
from moto import Moto

def main()-> None:
    #Automovil
    automovil = Automovil(4, "Azul")
    automovil.info()

    #Bicicleta
    bicicleta = Bicicleta(2, "Rojo")
    bicicleta.info()

    #Camion
    camion = Camion(8, "Negro")
    camion.info()

    #Moto
    moto = Moto(2, "Naranja")
    moto.info()

if __name__ == "__main__":
    main()