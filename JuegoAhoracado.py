import random
import string
from Palabras import palabras
from DiagramaAhorcado import vidas_diccionario_visual

def obtenerPalabra(palabras):
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():
    print("=========================")
    print("¡Bienvenid@ al juego del Ahorcado!")
    print("=========================")

    palabra = obtenerPalabra(palabras)

    letrasPorAdivinar = set(palabra)
    letrasAdivinadas = set()
    abecedario = set(string.ascii_uppercase) # no contiene ñ

    vidas = 7

    while len(letrasPorAdivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letrasAdivinadas)}")

        palabraLista = [letra if letra in letrasAdivinadas else '_' for letra in palabra]

        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabraLista)}")

        letraUsuario = input("Escoge una letra: ").upper()

        if letraUsuario in abecedario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)

            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print('')
            else:
                vidas -= 1
                print(f"\nTu letra, {letraUsuario} no está en la palabra.")
        elif letraUsuario in letrasAdivinadas:
            print("\Ya escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"¡Excelente! Adivinaste la palabra {palabra}")

ahorcado()