import random

# Creamos la clase Ahorcado y se crean en primer lugar los atributos
class Ahorcado:
    def __init__(self):
        self.palabras = ['moñiga', 'puchero', 'paliza', 'croqueta', 'cazurro', 'calvo']
        self.palabra = random.choice(self.palabras)
        self.letras_adivinadas = []
        self.intentos = 6

    # Método para crear el tablero que utilizaremos en el programa

    def mostrar_tablero(self):
        figura = [
            '''
             -----
             |   |
                 |
                 |
                 |
            ========
            ''',
            '''
             -----
             |   |
             |   0
                 |
                 |
            ========
            ''',
            '''
             -----
             |   |
             |   0
             |   |
                 |
            ========
            ''',
            '''
             -----
             |   |
             |   0
             |  /|
                 |
            ========
            ''',
            '''
             -----
             |   |
             |   0
             |  /|\\
                 |
            ========
            ''',
            '''
             -----
             |   |
             |   0
             |  /|\\
             |  /
            ========
            ''',
            '''
             -----
             |   |
             |   0
             |  /|\\
             |  / \\
            ========
            ''',
        ]

    # Verificamos en este if si el número de intentos actual (self.intentos)
    # que la longitud de la lista figura, y mostramos la representación gráfica correspondiente a
    # la posición actual de la etapa del juego
        if self.intentos < len(figura):
            print(figura[self.intentos])
        else:
            return figura[-1]

    # Este método que creo es para procesar cada letra dada por el jugador está dentro de
    # la palabra que el programa a elegido de forma aleatoria dentro de las palabras dadas en el
    # atributo (self.palabras) si esto no se cumple se reduce el numero de intentos en
    def adivinar_letra(self, letra):
        if letra in self.palabra and letra not in self.letras_adivinadas:
            self.letras_adivinadas.append(letra)
        else:
            self.intentos -= 1

    # Método principal con el menú del juego, que interactuará con los otros métodos creados
    # para ir desarrollando el ejercicio
    def jugar(self):
        print('***Bienvenidos al juego del Ahorcado***')
        print('---------------------------------------')
        print('Adivina la palabra secreta antes de quedarte sin intentos o\nnuestro amigo la espicha...')

        # Este print es importante porque conseguiremos que se muestre un guión bajo en la letra correspondiente
        # de la palabra oculta
        print('Palabra Secreta: ', ''.join('_' for _ in self.palabra))

        # Este bucle se ejecuta mientras el juego está en curso
        while True:
            self.mostrar_tablero()
            letra = input(
                'Ingrese una letra: ').lower()

            # Verificar si la entrada del jugador es válida (una sola letra)
            if len(letra) != 1 or not letra.isalpha():
                print('Mete una letra válida cohone!')

            # Llamar al método adivinar_letra para procesar la letra ingresada
            self.adivinar_letra(letra)

            # Verificar si el jugador se quedó sin intentos
            if self.intentos == 0:
                print('Mala suerte pisha te quedaste sin intentos, la palabra secreta era: ', self.palabra)
                break

            # Crear una representación de la palabra oculta
            palabra_oculta = ''
            for letra_palabra in self.palabra:
                if letra_palabra in self.letras_adivinadas:
                    palabra_oculta += letra_palabra + ' '
                else:
                    palabra_oculta += '_ '

            # Verificar si todas las letras han sido adivinadas (no hay guiones bajos en palabra_oculta)
            if '_' not in palabra_oculta:
                print('Felicidades Crack! Acertaste la palabra oculta, el pibito está a salvo.')
                break

