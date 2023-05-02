import random
# Función que genera los números aleatorios para el bingo
def generador_numeros():
    numeros = random.sample(range(1, 91), 90)
    for numero in numeros:
        yield numero

# Función que crea los cartones
def crear_cartones():
    cartones = {}
    for i in range(1, 4):
        if i == 1:
            num_cartones = 3
        elif i == 2:
            num_cartones = 2
        else:
            num_cartones = 1

        cartones_jugador = []
        for j in range(num_cartones):
            carton = []
            for rango in range(10, 100, 10):
                numeros_rango = random.sample(range(rango, rango+10), 2)
                carton.extend(numeros_rango)

            # Añadimos el número 90 al último rango
            carton[-1] = 90
            # Ordenamos el cartón de forma ascendente
            carton.sort()

            cartones_jugador.append(carton)
        
        cartones[f"Jugador{i}"] = cartones_jugador
    
    return cartones

# Función que comprueba si un número ha sido tachado en un cartón
def tachar_numero(carton, numero):
    if numero in carton:
        indice = carton.index(numero)
        carton[indice] = 'X'
        return True
    else:
        return False

# Función que comprueba si un jugador ha ganado con algún cartón
def comprobar_ganador(cartones):
    for jugador, cartones_jugador in cartones.items():
        for i, carton in enumerate(cartones_jugador):
            # Comprobamos filas
            if all(num == 'X' for num in carton[0:9:3]) or all(num == 'X' for num in carton[1:10:3]) or all(num == 'X' for num in carton[2:11:3]):
                return jugador, i+1
            # Comprobamos columnas
            elif all(num == 'X' for num in [carton[0], carton[3], carton[6]]) or all(num == 'X' for num in [carton[1], carton[4], carton[7]]) or all(num == 'X' for num in [carton[2], carton[5], carton[8]]):
                return jugador, i+1
            # Comprobamos diagonales
            elif all(num == 'X' for num in [carton[0], carton[4], carton[8]]) or all(num == 'X' for num in [carton[2], carton[4], carton[6]]):
                return jugador, i+1

    return None, None
# Función principal que juega una partida de bingo
def jugar_bingo():
    # Creamos los cartones
    cartones = crear_cartones()

    # Inicializamos el generador de números
    numeros = generador_numeros()

    # Inicializamos la lista de números que han ido saliendo
    numeros_sacados = []

    # Jugamos hasta que haya un ganador
    while True:
        # Sacamos un número del generador de números
        numero = next(numeros)

        # Añadimos el número a la lista de números sacados
        numeros_sacados.append(numero)

        # Imprimimos el número
        print(f"\nNúmero sacado: {numero}\n")

        # Tachamos el número en los cartones de todos los jugadores
        for jugador, cartones_jugador in cartones.items():
            print(f"Cartones del jugador {jugador}:")
            for i, carton in enumerate(cartones_jugador):
                if tachar_numero(carton, numero):
                    print(f"  Cartón {i+1}: {carton}  <------------------------ Tachado el {numero} :)!")
                else:
                    print(f"  Cartón {i+1}: {carton}")
            # Comprobamos si el jugador ha ganado con alguno de sus cartones
            ganador, carton = comprobar_ganador(cartones)
            if ganador is not None:
                print(f"\n¡El ganador es el {ganador} con el cartón {carton} :D :D :D :D !")
                print (f"\nLos números ganadores han salido en las siguiente posiciones: {numeros_sacados}")
                print("Presiona la tecla ENTER para salir del juego")
                return

# Llamamos a la función jugar_bingo para que se ejecute el juego
jugar_bingo()
