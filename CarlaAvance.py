def ejecutar_instrucciones():
    entrada = input("¿Quién inicia el juego? 1.-Máquina(Yo) 0.-Oponente")

    if entrada == '1':
        # Instrucciones si se ingresa '1'
        print("Mi tiro es:")
        # Aquí colocarías las instrucciones que deseas ejecutar si se ingresa '1'

    elif entrada == '0':
        # Instrucciones si se ingresa '0'
        print("¿Dónde colocó su tiro? (Ingresa la posición del tablero general)")
        posGeneral = input("Tablero General")
        posmini = input("Tablero mini")
        
        # Aquí colocarías las instrucciones que deseas ejecutar si se ingresa '0'

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
        return letra_mayuscula + letra_minuscula



#ejecutar_instrucciones()
# Ejemplo de uso
i = 1
j = 1
resultado = convertirIJ(i, j)
print(resultado)  # Salida: Aa
        
