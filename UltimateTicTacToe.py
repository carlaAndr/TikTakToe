# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""

Primeros pasos para el juego del gato
1- Funcion minimax para ver como funciona
2- Funcion minimax pero con poda alfa beta, que es mas eficiente
3- Una idea de como podria ser nuestro nodo
4- Para imprimir el gato jaja

"""
import numpy as np 

class nodoGato:
    def inicializar (self, turno, tablero, gatosInternos, espaciosDisp, hijos):
        self.miTurno = turno #Especifica de quien es el turno
        self.tableros = [0,0,0,0,0,0,0,0,0] #Aun no se como representar el tablero, pero puede ser asi
        self.gatosInternos = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        self.espaciosDisp = espaciosDisp #Nos dice cuandos espacios tenemos disponibles para tirar (como representar)
        self.hijos = [] #Los hijos de cada nodo

        
        

def miniMax (nodo, profundidad, turnoMax): #Aqui Max somos nosotros, necesitamos 
    if profundidad == 0 or estadoFinal(nodo):
        return funcionHeuristica(nodo) #Saber cuando vale en donde nos quedamos 
    if turnoMax:
        valorMax = - np.inf #Tener un parametro lo mas bajo posible
        for hijo in nodo:
            evaluar = miniMax(nodo, profundidad - 1, False) #Es false porque no es el turnno del rival
            valorMax = max (valorMax, evaluar)
        return valorMax
    else:
        valorMin = np.inf #Tener un parametro lo mas alto posible
        for hijo in nodo:
            evaluar = miniMax(nodo, profundidad - 1, True) #Si es turno del rival
            valorMin = min (valorMin, evaluar)
        return valorMin
        

#Una variacion que nos va a permitir ahorrar tiempo en la busqueda
#Inicializamos de una vez alfa en - infinito y beta en infinito        
def AlfaBetaMiniMax (nodo, profundidad, alfa, beta, turnoMax):
    if profundidad == 0 or estadoFinal (nodo):
        return funcionHeuristica(nodo) #saber cuanto vale en donde nos quedamos 
    if turnoMax: 
        valorMax = - np.inf
        for hijo in nodo:
            evaluar = AlfaBetaMiniMax(nodo, profundidad-1, alfa, beta, False)
            valorMax = max(valorMax, evaluar)
            alfa = max (alfa, evaluar)
            if beta <= alfa:
                break #No conviene seguir explorando, pues ya hay una mejor opcion
        return valorMax
    else:
        valorMin= np.inf
        for hijo in nodo:
            evaluar = AlfaBetaMiniMax(nodo, profundidad-1, alfa, beta, True)
            valorMin= min (valorMin, evaluar)
            beta = min (beta, evaluar)
            if beta <= alfa:
                break #No conviene seguir explorando
        return valorMin
        
    
    
#Saber que tan bueno es el estado actual    
def funcionHeuristica (nodo):
    return 1
#Saber si ya ganamos o perdimos             
def estadoFinal (nodo):
    return True

def imprimetablero ():
    i = ("\n ' ' | ' ' | ' ' \n"
         "\n ' ' | ' ' | ' ' \n" 
         "\n ' ' | ' ' | ' ' \n")
    for j in range(9):
        if j % 3 == 0:
            print ("_______________")
        print ("\n " + i + "\n")
        
        
def imprimeNodoGato (nodo):
    for i in len(nodo.tableros):
        print ("\n")
        print (nodo.gatosInternos[i])
        print ("\n")
        
        
gato = nodoGato()
print (imprimeNodoGato(gato))




