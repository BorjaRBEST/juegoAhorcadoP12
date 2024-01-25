import random

# Creamos la clase Ahorcado y se crean en primer lugar los atributos
class Ahorcado:
    def __init__(self):
        self.palabras = ['Aquí se agregan tantas palabras como queramos']
        self.palabra = random.choice(self.palabras)
        self.letras_adivinadas = []
        self.intentos = 6

    # Método para crear el tablero que utilizaremos en el programa

    def mostrar_tablero(self):
        figura = [
            '''
            Aquí vamos a agregar nuestros modelos visuales de muñecos
            
            ''',


        ]

    # Verificamos en este if si el número de intentos actual (self.intentos)
    # que la longitud de la lista figura, y mostramos la representación gráfica correspondiente a
    # la posición actual de la etapa del juego
        if self.intentos < len(figura):
            print(figura[self.intentos])

    # Este método que creo es para procesar cada letra dada por el jugador está dentro de
    # la palabra que el programa a elegido de forma aleatoria dentro de las palabras dadas en el
    # atributo (self.palabras) si esto no se cumple se reduce el numero de intentos en -1

    def adivinar_letra(self, letra):
        if letra in self.palabra and letra not in self.letras_adivinadas:
            self.letras_adivinadas.append(letra)
        else:
            self.intentos -= 1

