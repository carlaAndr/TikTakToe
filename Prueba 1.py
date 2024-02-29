class nodoGato:
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
        self.valor_heuristico = valor_heuristico # Valor  heurístico del estado actual

 # Mientras el juego no termine el ciclo continuará
 #Aquí habría que meter todas las cosas que decida el jugador
 
def dinamicaJuego (nodo,termino,turno):
    while not termino:
    #turno Verdadero
        if (turno):
            #Me toca tirar a mi
            print("Me toca tirar: ")
            #Tiro FUNCION CON TODO #MERGE
            #tiro
            iX=par[0]
            iY=par[1]
            #1 indica que cada nosotros tiramos en esas posición
            nodo.gatosInternos[iX][iY]=1

            
            turno=False;
        else:
            posiciones = input("Ingresa el tiro del oponente: ")
            posiciones_separadas = posiciones.split()  # Separar la cadena en dos partes utilizando el espacio como delimitador
                       
            par=convertirAB(posiciones_separadas[0],posiciones_separadas[1])
            #Este modifica directamente el gato en el que nos encontramos !!!!!!
            iX=par[0]
            iY=par[1]
            #-1 indica que el otro jugador tiró
            nodo.gatosInternos[iX][iY]=-1


            

            turno=True;


#Recibe un par de números (coordenadas del gato) y genera su posición como una combinación de letras
#Mayúscula para el gato general y minúscula para el pequeño

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
#Imagen de bienvenida
def dibujar_gato():
    gato = r'''
    /\_/\ 
    ( o.o )             ***  ¡ Bienvenido a Ultimate Tic Tac Toe ! ***
    > ^ <
        '''
    print(gato)
    print(" /~~~~\\")
    print("(_    _)")
    print("  \  /")
    print("   ||")
    print("   ||")
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

#Comienza las instrucciones
def ejecutar_instrucciones(nodo):
    #Imprime el gato
    dibujar_gato()
    turno=True
    #Inicializa todos los elementos del gato
    mi_gato = nodoGato()
    
    entrada = input("¿Quién inicia el juego? 1.-Máquina(Yo) 0.-Oponente:  ")
    if entrada == '1':
        # Aquí colocarías las instrucciones que deseas ejecutar si se ingresa '1'
        dinamicaJuego(nodo=mi_gato,termino=False,turno=turno)

    elif entrada == '0':
        # Instrucciones si se ingresa '0'
        print("¿Dónde colocó su tiro? (Ingresa la posición del tablero general y del tablero mini, separadas por un espacio)")
        posiciones = input("Posiciones (general mini): ")
        posiciones_separadas = posiciones.split()  # Separar la cadena en dos partes utilizando el espacio como delimitador
 
        par=convertirAB(posiciones_separadas[0],posiciones_separadas[1])
        #Este modifica directamente el gato en el que nos encontramos !!!!!!
        iX=par[0]
        iY=par[1]
        nodo.gatosInternos[iX][iY]=-1
        print("Gato", nodo.gatosInternos)
        dinamicaJuego(nodo=mi_gato,termino=False,turno=turno)
        
        if len(posiciones_separadas) != 2:
            print("Error: Debes ingresar dos posiciones separadas por un espacio.")
 
    else:# En caso de que se ingrese un valor diferente de '1' o '0'
        print("Entrada inválida. Por favor ingresa solo 1 o 0.")   

   
mi_gato = nodoGato()

ejecutar_instrucciones(mi_gato)


