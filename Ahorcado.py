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