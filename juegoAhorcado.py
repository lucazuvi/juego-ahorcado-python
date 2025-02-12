

import random


def obtenerPalabraSecreta() -> str:
    palabras = ['phyton', 'java', 'javascript', 'typescript', 'ruby','react','cobol','assembler', 'angular']
    return random.choice(palabras)



def mostrarProgreso(palabraSecreta, letrasAdivinadas):
    adivinado = ''

    for letra in palabraSecreta:
        if letra in letrasAdivinadas:
            adivinado += f" {letra} "
        else:
            adivinado += ' _ '
    
    return adivinado



def juegoAhorcado():
    palabraSecreta = obtenerPalabraSecreta()
    letrasAdivinadas = []
    intentos = 7
    juegoTerminado = False


    print('Bienvenido al juego del ahorcado!')
    print(f'Tenes {intentos} intentos para adivinar la palabra secreta')
    print(mostrarProgreso(palabraSecreta, letrasAdivinadas), "La palabra tiene",len(palabraSecreta),"letras.")

    while not juegoTerminado and intentos > 0:
        adivinanza = input('Introduzca una letra: ').lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print('Por favor, introduzca una letra valida! (solo una)')
        elif adivinanza in letrasAdivinadas:
            print('Ya usaste esa letra, proba con otra. ')
        else:
            letrasAdivinadas.append(adivinanza)

            if adivinanza in palabraSecreta:
                print(f"Muy bien! La letra '{adivinanza}' esta: ")
                if palabraSecreta.count(adivinanza) > 1:
                    print(f"{palabraSecreta.count(adivinanza)} veces en la palabra!")
                else:
                    print(f"{palabraSecreta.count(adivinanza)} vez en la palabra!")
            else:
                intentos -= 1
                print(f"La letra {adivinanza} no esta en la palabra secreta." )
                print(f"Te quedan {intentos} intentos.")
        
        progresoActual = mostrarProgreso(palabraSecreta, letrasAdivinadas)
        print(progresoActual)

        if "_" not in progresoActual:
            juegoTerminado = True
            print(f"Felicidades! Has ganado. La palabra secreta es: '{palabraSecreta.capitalize()}'")

    if intentos == 0:
        print(f"Perdiste! La palabra secreta era: {palabraSecreta.capitalize()}.")

juegoAhorcado()


