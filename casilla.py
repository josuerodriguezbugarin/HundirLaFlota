class Casilla:
    #Representa una única coordenada dentro del tablero.
    #Actúa como contenedor de una nave y mantiene la 'memoria' de los disparos.
    def __init__(self):
        self.nave = None
        self.visitada = False

    def disparar(self):
        #gestiona la logica cuando el jugador ataca esta coordenada, devuelve: None si la casilla ua fue disparada
        #0 si es agua. 1 o 2 (Tocado o hundido) si hay una nave
        if self.visitada:
            print("Ya disparaste aquí")
            return None

        self.visitada = True

        if self.nave is None:
            print("Agua")
            return 0

        return self.nave.recibir_disparo()