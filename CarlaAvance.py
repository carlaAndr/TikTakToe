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

def ejecutar_instrucciones():
    dibujar_gato()
    entrada = input("¿Quién inicia el juego? 1.-Máquina(Yo) 0.-Oponente:  ")
    if entrada == '1':
        # Instrucciones si se ingresa '1'
        print("Mi tiro es:")
        # Aquí colocarías las instrucciones que deseas ejecutar si se ingresa '1'

    elif entrada == '0':
        # Instrucciones si se ingresa '0'
        print("¿Dónde colocó su tiro? (Ingresa la posición del tablero general, una letra a la vez)")
        posGeneral = input("Tablero General: ")
        posmini = input("Tablero mini: ")
        par=convertirAB(posGeneral,posmini) 
        #Aquí se asignaría a la posición en el gato.
    else:
        # En caso de que se ingrese un valor diferente de '1' o '0'
        print("Entrada inválida. Por favor ingresa solo 1 o 0.")   
    
def convertirIJ(i,j):
        #Main Mayus
        #mini, minusculas
        if i < 0 or i > 8 or j < 0 or j > 8:
            return "Entrada inválida. Los valores de i y j deben estar entre 1 y 26."
        letra_mayuscula = chr(65 + i)  # Convertir número a letra mayúscula ('A' es 65 en ASCII)
        letra_minuscula = chr(97 + j)  # Convertir número a letra minúscula ('a' es 97 en ASCII)
        return [letra_mayuscula, letra_minuscula]

def convertirAB(letra_mayuscula, letra_minuscula):
    if not ('A' <= letra_mayuscula <= 'I' and 'a' <= letra_minuscula <= 'i'):
        return "Entrada inválida. Las letras deben estar entre A y I en mayúsculas, y a y i en minúsculas."
    
    i = ord(letra_mayuscula) - 65  # Convertir letra mayúscula a número (A es 65 en ASCII)
    j = ord(letra_minuscula) - 97  # Convertir letra minúscula a número (a es 97 en ASCII)
    
    return [i, j]

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

def checarGanar(pos):
    return 1

#Main
#ejecutar_instrucciones()
arreglo = [0, 1, -1,
            0, -1, 1,
            0, 1,0]
arreglo1=[0,0,0,
          0,0,0,
          0,0,0]
arreglo2=[0,0,0,
          0,1,0,
          -1,-1,1]
print(evaluates(arreglo))
print(evaluates(arreglo1))
print(evaluates(arreglo2))

"""##function realEvaluateSquare(pos){
    #var evaluation = 0;
    #var points = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2];
    #
    #for(var bw in pos):
        #evaluation -= pos[bw]*points[bw];

    a = 2;
    if(gatopeq[0] + gatopeq[1] + gatopeq[2] == a or gatopeq[3] + gatopeq[4] + gatopeq[5] == a or gatopeq[6] + gatopeq[7] + gatopeq[8] == a): 
        evaluation -= 6;
        #Le resto 6 porque
    
    if(gatopeq[0] + gatopeq[3] + gatopeq[6] == a or gatopeq[1] + gatopeq[4] + gatopeq[7] ==a or gatopeq[2] + gatopeq[5] + gatopeq[8] == a): 
        evaluation -= 6;
   
    if(gatopeq[0] + gatopeq[4] + gatopeq[8] == a || gatopeq[2] + pos[4] + pos[6] === a) {
        evaluation -= 7;
    }

    a = -1;
    
    if((pos[0] + pos[1] === 2*a && pos[2] === -a)      || (pos[1] + pos[2] === 2*a && pos[0] === -a) || (pos[0] + pos[2] === 2*a && pos[1] === -a)
        || (pos[3] + pos[4] === 2*a && pos[5] === -a) || (pos[3] + pos[5] === 2*a && pos[4] === -a) || (pos[5] + pos[4] === 2*a && pos[3] === -a)
        || (pos[6] + pos[7] === 2*a && pos[8] === -a) || (pos[6] + pos[8] === 2*a && pos[7] === -a) || (pos[7] + pos[8] === 2*a && pos[6] === -a)
        || (pos[0] + pos[3] === 2*a && pos[6] === -a) || (pos[0] + pos[6] === 2*a && pos[3] === -a) || (pos[3] + pos[6] === 2*a && pos[0] === -a)
        || (pos[1] + pos[4] === 2*a && pos[7] === -a) || (pos[1] + pos[7] === 2*a && pos[4] === -a) || (pos[4] + pos[7] === 2*a && pos[1] === -a)
        || (pos[2] + pos[5] === 2*a && pos[8] === -a) || (pos[2] + pos[8] === 2*a && pos[5] === -a) || (pos[5] + pos[8] === 2*a && pos[2] === -a)
        || (pos[0] + pos[4] === 2*a && pos[8] === -a) || (pos[0] + pos[8] === 2*a && pos[4] === -a) || (pos[4] + pos[8] === 2*a && pos[0] === -a)
        || (pos[2] + pos[4] === 2*a && pos[6] === -a) || (pos[2] + pos[6] === 2*a && pos[4] === -a) || (pos[4] + pos[6] === 2*a && pos[2] === -a)){
        evaluation-=9;
    }

    a = -2;
    if(pos[0] + pos[1] + pos[2] === a || pos[3] + pos[4] + pos[5] === a || pos[6] + pos[7] + pos[8] === a) {
        evaluation += 6;
    }
    if(pos[0] + pos[3] + pos[6] === a || pos[1] + pos[4] + pos[7] === a || pos[2] + pos[5] + pos[8] === a) {
        evaluation += 6;
    }
    if(pos[0] + pos[4] + pos[8] === a || pos[2] + pos[4] + pos[6] === a) {
        evaluation += 7;
    }

    a = 1;
    if((pos[0] + pos[1] === 2*a && pos[2] === -a) || (pos[1] + pos[2] === 2*a && pos[0] === -a) || (pos[0] + pos[2] === 2*a && pos[1] === -a)
        || (pos[3] + pos[4] === 2*a && pos[5] === -a) || (pos[3] + pos[5] === 2*a && pos[4] === -a) || (pos[5] + pos[4] === 2*a && pos[3] === -a)
        || (pos[6] + pos[7] === 2*a && pos[8] === -a) || (pos[6] + pos[8] === 2*a && pos[7] === -a) || (pos[7] + pos[8] === 2*a && pos[6] === -a)
        || (pos[0] + pos[3] === 2*a && pos[6] === -a) || (pos[0] + pos[6] === 2*a && pos[3] === -a) || (pos[3] + pos[6] === 2*a && pos[0] === -a)
        || (pos[1] + pos[4] === 2*a && pos[7] === -a) || (pos[1] + pos[7] === 2*a && pos[4] === -a) || (pos[4] + pos[7] === 2*a && pos[1] === -a)
        || (pos[2] + pos[5] === 2*a && pos[8] === -a) || (pos[2] + pos[8] === 2*a && pos[5] === -a) || (pos[5] + pos[8] === 2*a && pos[2] === -a)
        || (pos[0] + pos[4] === 2*a && pos[8] === -a) || (pos[0] + pos[8] === 2*a && pos[4] === -a) || (pos[4] + pos[8] === 2*a && pos[0] === -a)
        || (pos[2] + pos[4] === 2*a && pos[6] === -a) || (pos[2] + pos[6] === 2*a && pos[4] === -a) || (pos[4] + pos[6] === 2*a && pos[2] === -a)){
        evaluation+=9;
    }
    #Checar ganar

    evaluation -= checarGanar(pos)*12;
    return evaluation """
    
    