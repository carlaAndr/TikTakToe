# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:08:11 2024

@author: Diego
"""

'''
Nueva version ajustando algunas cosas para que me sea mas facil acceder a ciertas cosas

'''

import numpy as np
#import copy

"""
Clase nodoGato
Se trata de lo que va a representar nuestro tablero, cuenta con
- turno: Marca a quien le toca tirar, su valor sera de -1 si le toca al rival y de 1 si nos toca a nosotros
- tableros: Se trata de un arreglo y representa el macrogato, se inicializa con 0s (neutral) y si alguno de esos gatos
    llegara a ser ganado por alguien, se pone 1 si fue por el jugador o -1 si fue por el rival
- gatosInternos: Un arreglo de arreglos, cada arreglo representa un gato pequenio, al igual que en tableros, 0 es un espacio disponible
    1 si ganamos la posicion y -1 si el rival la tomo
- espacios disponibles: un arreglo con 9 posiciones que representa el numero de espacios disponibles en cada minigato, por defecto, entonces
    se inicializan todos en 9, cada turno, se le resta la posicion que se ocupo
- valor heuristico: cada nodo tiene un valor y con ello decidimos que movimiento hacer 

"""
class nodoGato:

    """
    Constructor
    """
    def __init__(self, turno=0, tableros=None, gatosInternos=None, espaciosDisp=None, hijos=None, valor_heuristico=0):
        if tableros is None: # Tablero vacío inicial
            tableros = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
        if gatosInternos is None: # Gatos internos vacíos iniciales
            gatosInternos = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)] 
        if espaciosDisp is None: # Espacios disponibles completos para cada gato
            espaciosDisp = [9 for i in range(9)]
        if hijos is None: # Lista vacía de hijos
            hijos = []
        
        self.turno = turno # Especifica de quien es el turno
        self.tableros = tableros # Representacion del tablero
        self.gatosInternos = gatosInternos # Matriz que representa el juego actual
        self.espaciosDisp = espaciosDisp # Arreglo de espacios disponibles para cada gato
        self.hijos = hijos # Arreglo de hijos del nodo
        self.valor_heuristico = valor_heuristico # Valor  heurístico del estado actual // Es un arreglo para despues acceder a ellos facilmente 
        #Incluir un parametro extra en el constructor para tener siempre disponible jugada 
        self.jugadaAnterior= ()
        self.tiroActual = () #Necesito rescatar esta tupla porque es lo que voy a arrojar para tirar en los hijos
        #self.tiroActual = ()
        
#Metodos en la clase gato:       
    
    
    """
    Este es equivalente a un "get hijos". 
    Genera todos los movimientos posibles desde el estado actual del juego.

    Parametros:
        - jugada: [tupla] jugada previa (pos gatoExterior, pos gatoInterior)
        - turno: [int] (1 o -1 para cada jugador)
    Return:
        - Nodos de posibles movimientos
    """
    
    def movimientosPosibles(self, turno): #Aqui podriamos llamar al atributo jugada anterior y ya esta
            
        # Llamamos al tablero y juegos internos del nodo
        tablero = self.tableros
        juego  = self.gatosInternos
        espaciosDisp = self.espaciosDisp
        

        gato_interno = juego[self.jugadaAnterior[1]] # Llamamos al gato interno de la jugada previa, necesitamos el # del gato interno pasado
        movimientos =[] # Arreglo para almacenar nodos hijos

        # Regresa los índices de los espacios vacíos del gato interno
        blanks = [i for i, valor in enumerate(gato_interno) if valor == 0]

            # Para cada espacio vacío
        for espacio in blanks:
            juego_hijo = juego.copy() # Copiamos el juego
            gato_hijo = gato_interno.copy() # Copiamos el gato interno
            gato_hijo[espacio] = turno # Marcamos el movimiento en el gato interno

            juego_hijo[self.jugadaAnterior[1]] = gato_hijo # Sustituímos el gato interno por el del nuevo movimiento
            
                # Crea el nuevo nodo
            nuevo_nodo = nodoGato(turno=-(turno), # Determinamos que el turno es del siguiente jugador
                                    tableros=tablero, # Tablero se queda igual
                                    gatosInternos=juego_hijo, # Se determina el nuevo juego modificado
                                    espaciosDisp=(espaciosDisp[self.jugadaAnterior[1]] - 1), # Le restamos un espacio disponible al gato interno 
                                    valor_heuristico=self.valor_heuristico) # Dejamos el valor heurístico como está
            nuevo_nodo.tiroActual = (self.jugadaAnterior[1], espacio)
            movimientos.append(nuevo_nodo)
        return movimientos
         
    """
    Esta función verifica si una jugada se puede realizar en un tablero específico del gato.
    No se puede jugar en un gato interno que haya sido totalmente ocupado o que ya lo haya ganado un jugador.

    Parámetros:
        - jugada: [tupla] jugada previa (pos gatoExterior, pos gatoInterior)
    Return:
        - valid: [booleano] regresa si es válido jugar en el gato interno.
    """
    # Puedo usar la bandera en el segundo if
    def validarJugada(self, jugada):
        valid = True
        tablero = self.tableros # Llamamos al tablero
        if(tablero[jugada[0]] != 0): # Si el gato interno ya está ganado por un jugador, no se puede jugar ahí
            valid = False
        gato_interno = self.gatosInternos[jugada[0]] # Llamamos al gato interno
        if(all(valor != 0 for valor in gato_interno)): # Si ya se tiró en todas las casillas, no se puede jugar ahí
            valid = False
        return valid
    
    
    """
    Esta función evalúa si el nodo es un Estado Final.

    Regresa fin [booleano]: indica si ya se terminó el juego.
    """
    # Puedo usar la bandera en el segundo if
    def estadoFinal(self):
        fin = False

        tablero = self.tableros # Llamamos al tablero
        ganador = checarGanar(tablero) # Verificamos si hay un ganador
        
        #Checamos:
        if(ganador != 0): # Si ya se ganó el juego
            fin = True
        if(all(valor != 0 for valor in tablero)): # Si ya se llenó el gato
            fin = True

        return fin  
    """
    Esta funcion permite modificar los gatosInternos, ya sea para el movimiento de un rival o incluso mio
    posiciones debe ser una tupla de la forma: (X, y), es decir pos en gatoGrande, pos en gatoPequenio (no letras, numeros) y solo 0 <=valores<= 8
    Debemos especificar por cual valor va a sustituir el 0 que esta por defecto (1 fue nuestro turno, -1 tiro el rival)
    Ademas registra ese movimiento que se acaba de hacer, para que otros metodos que piden la jugada anterior puedan acceder
    Y para que haya congruencia, una vez que efectuo el movimiento, cambia automaticamente el turno 
    """
    #Para facilitar la edicion en movimientos del rival, modifico directamente (y tambien para reflejar los mios)
    #Voy a recibir una tupla que me indique los lugares a modificar 
    #Las posiciones deben tener un valor entre 0  8
    #El turno es para saber que numero voy a poner en ese lugar
    def modificaTableroDirecto(self, posiciones, turno):
        p1 = posiciones[0]
        p2 = posiciones[1]
        if self.validarJugada((p1,p2)):
            self.gatosInternos[p1][p2] = turno
            self.espaciosDisp[p1] = self.espaciosDisp[p1] -1
            self.jugadaAnterior = (p1, p2)
            #Despues de modificar el gato, necesito cambiar el turno
            self.turno = turno * -1
    """
    Determina que tanto vale el nodo actual dependiendo de la funcion heuristica, que dentro de ella ya ha evaluado el gatoGrande y gatosPequenios
    """    
    #Lo voy a hacer dentro de cada nodo para que despues solo tenga que consultar el atributo del nodo    
    def determinaValorHeuristico (self):
        valor = evaluar_juego(self.gatosInternos)
        self.valor_heuristico = valor[0]
        return valor[0]
    """
    Se encarga de hacer un listado con todos los hijos posibles del nodo, ya que el arreglo de hijos esta vacio previamente
    """
    #Para que haga los hijos solito
    def enlistaHijos(self):
        self.hijos = self.movimientosPosibles(self.turno)
    
    """
    Si hay que hacer alguna modificacion al turno, por si acaso, tenemos esta funcion
    """
    def cambiaTurnoNodo (self, nuevoTurno):
        if nuevoTurno == 1 or nuevoTurno == -1:
            self.turno = nuevoTurno
    """    
    def reglaCorrespondencia(self):
        posicion = self.jugadaAnterior
        siguienteRecuadro = posicion[1]
        return siguienteRecuadro
    
    def tiroActual (self):
        return self.tiroActual
    """
    """
    Se encarga de explorar todos los hijos, que junto a la funcion heuristica, se encarga de decidir como vamos a jugar de acuerdo a los valores
        del nodo
    """
    def mejorTiro (self):
        hijos = self.enlistaHijos()
        valorMax = np.inf
        tiroFinal = ()
        for hijo in self.hijos:
            valorHijo = hijo.determinaValorHeuristico()
            if valorHijo < valorMax:
                valorMax = valorHijo
                tiroFinal = hijo.tiroActual
        if self.validarJugada(tiroFinal):
            self.tiroActual = tiroFinal
            return tiroFinal
        else:                           #Si no se puede jugar el nodo ideal, tira cualquier otro que tenga de alternativa pero que no sea igual
            for hijo in self.hijos:
                alternativa = hijo.tiroActual
                if hijo.alternativa != tiroFinal and self.validarJugada(alternativa):
                    self.tiroActual = alternativa 
                    return alternativa
                break
    
"""
Empiezan otras funciones utiles para la implementacion de nuestro sistema
"""                
                 

"""
Dos funciones que se encargan de traducir los tiros del rival que nos son expresados en letras (A,a) a numeros 
    para las tuplas requeridas = convertir AB.
    O de transformar nuestro tiro visto como tupla a letras para la facilidad del contrincante = convertirIJ
"""
def convertirIJ(i,j):
    if i < 0 or i > 8 or j < 0 or j > 8:
        return "Entrada inválida. Los valores de i y j deben estar entre 1 y 26."
    letra_mayuscula = chr(65 + i)  # Convertir número a letra mayúscula ('A' es 65 en ASCII)
    letra_minuscula = chr(97 + j)  # Convertir número a letra minúscula ('a' es 97 en ASCII)
    return [letra_mayuscula, letra_minuscula]
#Recibe un par de letras y regresa su posición en un arreglo de números.
#Primera para el gato general y la segunda para el pequeño
def convertirAB(letra_mayuscula, letra_minuscula):
    if not ('A' <= letra_mayuscula <= 'I' and 'a' <= letra_minuscula <= 'i'):
        return "Entrada inválida. Las letras deben estar entre A y I en mayúsculas, y a y i en minúsculas."
    i = ord(letra_mayuscula) - 65  # Convertir letra mayúscula a número (A es 65 en ASCII)
    j = ord(letra_minuscula) - 97  # Convertir letra minúscula a número (a es 97 en ASCII)
    return [i, j]

"""
Verifica si hay algún ganador en un juego de gato.

Parametros:
    - gatoInterno: [arreglo] es el juego de gato a evaluar
Return:
    - [int] El jugador ganador (1 o -1), o 0 si no hay ganador
"""

def checarGanar(gatoInterno):
    # Posibles combinaciones ganadoras
    combinaciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]

    # Verifica cada combinación para ambos jugadores
    for jugador in [1, -1]: # [ Jugadores ]
        for c in combinaciones_ganadoras:
            if all(gatoInterno[i] == jugador for i in c):
                return jugador

    # Si no se encuentra ganador, retorna 0
    return 0

"""
Se trata de nuestra funcion heuristica, que es aplicada a cada uno de los gatosPequenios del nodo, aqui vemos las cosas a nivel micro
"""

def evaluates(gatopeq):
    #Tiros: 1 (nosotros), -1(rival)
    evaluation=0
    points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2]
    for bw in gatopeq:
        #bw iría en [0,8]
        evaluation=evaluation-gatopeq[bw]*points[bw]
        #print(bw,"  ",evaluation)
    a=2
    #Puede ganar, hay un espacio vacío con dos 'segudis/diagonales' correspondientes a mi signo.
    if(gatopeq[0] + gatopeq[1] + gatopeq[2] == a or gatopeq[3] + gatopeq[4] + gatopeq[5] == a or gatopeq[6] + gatopeq[7] + gatopeq[8] == a):
        evaluation= evaluation-6
        #Le resto 6 porque
    if(gatopeq[0] + gatopeq[3] + gatopeq[6] == a or gatopeq[1] + gatopeq[4] + gatopeq[7] ==a or gatopeq[2] + gatopeq[5] + gatopeq[8] == a):
        evaluation= evaluation-6
    if(gatopeq[0] + gatopeq[4] + gatopeq[8] == a or gatopeq[2] + gatopeq[4] + gatopeq[6] == a):
        evaluation=evaluation-7
    a = -1
    #Ya se he bloquedo (por lo menos ) una de las líneas para ganar (Menor posibilidad de ganar)
    if((gatopeq[0] + gatopeq[1] == 2*a and gatopeq[2] == -a) or (gatopeq[1] + gatopeq[2] == 2*a and gatopeq[0] == -a) or (gatopeq[0] + gatopeq[2] == 2*a and gatopeq[1] == -a)
    or (gatopeq[3] + gatopeq[4] == 2*a and gatopeq[5] == -a) or (gatopeq[3] + gatopeq[5] == 2*a and gatopeq[4] == -a) or (gatopeq[5] + gatopeq[4] == 2*a and gatopeq[3] == -a)
    or (gatopeq[6] + gatopeq[7] == 2*a and gatopeq[8] == -a) or (gatopeq[6] + gatopeq[8] == 2*a and gatopeq[7] == -a) or (gatopeq[7] + gatopeq[8] == 2*a and gatopeq[6] == -a)
    or (gatopeq[0] + gatopeq[3] == 2*a and gatopeq[6] == -a) or (gatopeq[0] + gatopeq[6] == 2*a and gatopeq[3] == -a) or (gatopeq[3] + gatopeq[6] == 2*a and gatopeq[0] == -a)
    or (gatopeq[1] + gatopeq[4] == 2*a and gatopeq[7] == -a) or (gatopeq[1] + gatopeq[7] == 2*a and gatopeq[4] == -a) or (gatopeq[4] + gatopeq[7] == 2*a and gatopeq[1] == -a)
    or (gatopeq[2] + gatopeq[5] == 2*a and gatopeq[8] == -a) or (gatopeq[2] + gatopeq[8] == 2*a and gatopeq[5] == -a) or (gatopeq[5] + gatopeq[8] == 2*a and gatopeq[2] == -a)
    or (gatopeq[0] + gatopeq[4] == 2*a and gatopeq[8] == -a) or (gatopeq[0] + gatopeq[8] == 2*a and gatopeq[4] == -a) or (gatopeq[4] + gatopeq[8] == 2*a and gatopeq[0] == -a)
    or (gatopeq[2] + gatopeq[4] == 2*a and gatopeq[6] == -a) or (gatopeq[2] + gatopeq[6] == 2*a and gatopeq[4] == -a) or (gatopeq[4] + gatopeq[6] == 2*a and gatopeq[2] == -a)):
        evaluation=evaluation-9
    a=-2
    #El oponente puede ganar
    if(gatopeq[0] + gatopeq[1] + gatopeq[2] == a or gatopeq[3] + gatopeq[4] + gatopeq[5] == a or gatopeq[6] + gatopeq[7] + gatopeq[8] == a):
        evaluation =evaluation+6
    if(gatopeq[0] + gatopeq[3] + gatopeq[6] == a or gatopeq[1] + gatopeq[4] + gatopeq[7] == a or gatopeq[2] + gatopeq[5] + gatopeq[8] == a):
        evaluation=evaluation+6
    if(gatopeq[0] + gatopeq[4] + gatopeq[8] == a or gatopeq[2] + gatopeq[4] + gatopeq[6] == a):
        evaluation= evaluation+7

    a = 1
    #Me bloquearon
    if((gatopeq[0] + gatopeq[1] == 2*a and gatopeq[2] == -a) or (gatopeq[1] + gatopeq[2] == 2*a and gatopeq[0] == -a) or (gatopeq[0] + gatopeq[2] == 2*a and gatopeq[1] == -a)
    or (gatopeq[3] + gatopeq[4] == 2*a and gatopeq[5] == -a) or (gatopeq[3] + gatopeq[5] == 2*a and gatopeq[4] == -a) or (gatopeq[5] + gatopeq[4] == 2*a and gatopeq[3] == -a)
    or (gatopeq[6] + gatopeq[7] == 2*a and gatopeq[8] == -a) or (gatopeq[6] + gatopeq[8] == 2*a and gatopeq[7] == -a) or (gatopeq[7] + gatopeq[8] == 2*a and gatopeq[6] == -a)
    or (gatopeq[0] + gatopeq[3] == 2*a and gatopeq[6] == -a) or (gatopeq[0] + gatopeq[6] == 2*a and gatopeq[3] == -a) or (gatopeq[3] + gatopeq[6] == 2*a and gatopeq[0] == -a)
    or (gatopeq[1] + gatopeq[4] == 2*a and gatopeq[7] == -a) or (gatopeq[1] + gatopeq[7] == 2*a and gatopeq[4] == -a) or (gatopeq[4] + gatopeq[7] == 2*a and gatopeq[1] == -a)
    or (gatopeq[2] + gatopeq[5] == 2*a and gatopeq[8] == -a) or (gatopeq[2] + gatopeq[8] == 2*a and gatopeq[5] == -a) or (gatopeq[5] + gatopeq[8] == 2*a and gatopeq[2] == -a)
    or (gatopeq[0] + gatopeq[4] == 2*a and gatopeq[8] == -a) or (gatopeq[0] + gatopeq[8] == 2*a and gatopeq[4] == -a) or (gatopeq[4] + gatopeq[8] == 2*a and gatopeq[0] == -a)
    or (gatopeq[2] + gatopeq[4] == 2*a and gatopeq[6] == -a) or (gatopeq[2] + gatopeq[6] == 2*a and gatopeq[4] == -a) or (gatopeq[4] + gatopeq[6] == 2*a and gatopeq[2] == -a)):
        evaluation=evaluation+9


    evaluation=evaluation-checarGanar(gatopeq)*12;
    return evaluation

"""
Aqui, la funcion se encarga de evaluar tanto a nivel micro, como a nivel macro,
     es la funcion heuristica completa que el metodo del nodo 'mejorTiro' tomar en cuenta para decidir 
"""
# tableros representa el estado actual del juego en general (el super gato, arreglo de arreglos)
# tablero_actual es el índice del tablero pequeño en que el jugador debe jugar

#Por la dinamica de Genaro, entre numeros mas pequenios tengamos son los que vamos a elegir
def evaluar_juego(tableros):
    evaluacion_global = 0
    tablero_principal = [0] * 9  # Inicializa el tablero principal con 0s para representar que ningún mini-juego ha sido ganado aún.
    # Es necesario hacer las anteriores inicializaciones en cero para poder evaluar cada vez que le toque jugar, no influye si ya está iniciado el juego
    evaluaciones_mini_juegos = []  # Almacena la evaluación de cada mini-juego.
    multiplicadores = [1.4, 1, 1.4, 1, 1.75, 1, 1.4, 1, 1.4]  # Ponderaciones para cada mini-juego basadas en su importancia estratégica.
    # La importancia está dada por Centro:1.75, Esquinas: 1.4, Restantes: 1

    # Evalúa cada uno de los 9 mini-juegos (tableros pequeños).
    for i, tablero in enumerate(tableros):
        # Utiliza la función evaluates para obtener la evaluación del mini-juego actual.
        evaluacion_tablero = evaluates(tablero)
        # Ajusta la evaluación global sumando la evaluación del tablero actual multiplicada por su ponderación.
        evaluacion_global += evaluacion_tablero * 1.5 * multiplicadores[i]
        # El 1.5 es adicional para reflejar su ponderación con mayor diferencia.
        # Lo anterior refleja que no solo importa ganar o no ganar el mini gato, sino también el estado del juego.
        evaluaciones_mini_juegos.append(evaluacion_tablero)  # Guarda la evaluación de este mini-juego.

        # Utiliza la función checarGanar para determinar si hay un ganador en el mini-juego actual.
        ganador = checarGanar(tablero)
        if ganador != 0:
            # Si hay un ganador, actualiza el tablero principal para reflejar quién ha ganado el mini-juego.
            tablero_principal[i] = ganador
            evaluacion_global += ganador * multiplicadores[i] * 5000
            # Ajusta la evaluación global en función de quién ha ganado el mini-juego, usando la ponderación específica.
    # Evalúa el estado global del juego basado en el tablero principal.
    ganador_global = checarGanar(tablero_principal)  # Revisa si hay un ganador en el tablero principal.
    if ganador_global != 0:
        # Si hay un ganador global, ajusta significativamente la evaluación para reflejar esta victoria.
        evaluacion_global += ganador_global * 100000
    return evaluacion_global, evaluaciones_mini_juegos
    # Regresa tanto la evaluación global como la evaluación del estado actual de cada mini-gato
    


"""
Aqui las funciones son mas operativas, son el juego puesto en accion como tal
"""

"""
Imprime un gato bonito para ser mas amigable con el usuario
"""
def dibujarGato():
    gato = r'''
    /\_/\
    ( o.o )             
    > ^ <
*  ¡ Bienvenido a Ultimate Tic Tac Toe ! *
        '''
    print(gato)
    print("     /~~\\")
    print("   (_    _)")
    print("     \  /")
    print("      ||")
    print("     ||")

"""
Es la funcion que se va a correr y ejecutar, tiene los mensajes de bienvenida y otras dos funciones que se usaran dependiendo del turno inicial
"""
def ejecutarInstrucciones(nodo):
    dibujarGato()
    while True:
        entrada = input("¿Quién inicia el juego? Escribe '0' si somos nosotros. Ingresa '1' si es el rival:        ")
        if entrada.isdigit():
            menu = int(entrada)
            if menu == 0:
                first = True
                print("¡Nosotros iniciamos el juego!")
                nodo.cambiaTurnoNodo(1)
                dinamicaJugador(nodo, first)
                break
            elif menu == 1:
                first = False
                print("¡El rival inicia el juego!")
                procesar_movimiento_oponente(nodo)
                dinamicaJugador(nodo, first)
                break
            else:
                print("Tienes que ingresar un número válido, ya sea 0 o 1")
        else:
            print("Tienes que ingresar un número válido, ya sea 0 o 1")

""" 
Es la funcion que se ocupa para cuando sea nuestro turno de jugar despues del primer movimiento
Seguira corriendo hasta que no llegue a un estado final. Ademas, tiene una bandera booleana por si nosotros tiramos primero y asi ajustar al nodo
Puede soportar que los datos ingresados no tengan un espacio, pero se recomienda poner atencion al ingresar los datos
"""
def dinamicaJugador(nodo, primeraVez):
    termino = nodo.estadoFinal()
    while not termino:
        if nodo.turno == 1:
            if primeraVez:
                nodo.modificaTableroDirecto((4,4),1) #Siempre jugar en el centro del centro
                print ("\nMovimiento registrado")
                print ("El tiro se registro en: (4,4)")
                coor = convertirIJ(4, 4)
                print ("Coordenadas en letras:   " + coor[0] + " " +coor[1])
                
                primeraVez = False
            else:
                aTirar = nodo.mejorTiro()
                print("\nMovimiento registrado")
                print("El tiro se registró en: {} {}".format(aTirar[0], aTirar[1]))
                coor = convertirIJ(aTirar[0], aTirar[1])
                print ("Coordenadas en letras:   " +  coor[0] + " " +coor[1])
                nodo.modificaTableroDirecto(aTirar, 1) #Le indico el numero que va a poner en la posicion 
        else:
            #Significa que fue turno del jugador contrario y debo entonces 
            posiciones = input("\nIngresa el Tiro del oponente (Recuerda la nomenclatura y separalas por un espacio. Ejemplo: A a):          ")
            posiciones_separadas = posiciones.split()
            if len(posiciones_separadas) != 2:
                print("\nError: Debes ingresar dos posiciones separadas por un espacio.")
                continue  # Vuelve al inicio del bucle
            resultado_conversion = convertirAB(posiciones_separadas[0], posiciones_separadas[1]) #Convierte de letras a numeros
            if isinstance(resultado_conversion, list) and len(resultado_conversion) == 2:
                iX, iY = resultado_conversion                
                if nodo.validarJugada((iX, iY)):
                    nodo.modificaTableroDirecto((iX, iY), -1)
                else:
                    print("Movimiento inválido. Intenta de nuevo.")
                    continue
            else:
                print(resultado_conversion)
                continue
        termino = nodo.estadoFinal()

    print("El juego ha terminado.")    
"""
Funcion por si el primer turno fue del oponente, modifica el nodo de acuerdo al primer tiro del oponente
    Soporta que los datos ingresados no tengan un espacio entre ellos, pero se recomienda poner atencion al capturarlos
"""           
def procesar_movimiento_oponente(nodo):
    print("\n¿Dónde colocó su tiro el oponente?")
    print("\nIngresa [A a], donde 'A' es la posicion en el gato grande y 'a' en el gato pequenio, separadas por un espacio")
    posiciones = input("\nPosiciones (A, a):              ")
    posiciones_separadas = posiciones.split()

    if len(posiciones_separadas) != 2:
        print("\nError: Debes ingresar dos posiciones separadas por un espacio.")
        procesar_movimiento_oponente(nodo)  # Llamada recursiva si hay error
        return

    par = convertirAB(posiciones_separadas[0], posiciones_separadas[1]) #Convertir de letras a numeros
    iX, iY = par

    # Validar si el movimiento es posible
    if nodo.validarJugada((iX, iY)):
        nodo.modificaTableroDirecto((iX, iY), -1)  # -1 para el oponente
        print("\nMovimiento registrado.")
    else:
        print("\nMovimiento inválido. Intenta de nuevo.")
        procesar_movimiento_oponente(nodo)  # Llamada recursiva si el movimiento no es válido            
            
            
            
"""
Ejecutable: con estas dos lineas de codigo vamos a jugar Gato de gatos
"""
gato = nodoGato()
ejecutarInstrucciones(gato)
        
    