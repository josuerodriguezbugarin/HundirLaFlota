from tablero import Tablero

class Juego:

    #Conecta las acciones del jugador con el tablero y muestra los resultados.
    def __init__(self):
        self.tablero = Tablero()

    def mostrar_resultado(self, resultado):

        #Traduce el código numérico devuelto por la lógica del juego a texto legible.
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")
        elif resultado is None:
            print("Ya disparaste aquí")

    def lanzar_ataque(self, x, y):

        #Inicia el proceso de ataque en unas coordenadas específicas.
        print(f"\nAtaque en ({x},{y})")

        resultado = self.tablero.comprobar_impacto(x, y)

        self.mostrar_resultado(resultado)

    def jugar_demo(self):

        #Esto es como una demo que ejecuta una serie de disparos de prueba.
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1, 5)


if __name__ == "__main__":
    juego = Juego()
    juego.jugar_demo()