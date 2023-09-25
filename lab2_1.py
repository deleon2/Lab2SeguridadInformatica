# Universidad Finis Terrae
# Laboratorio N°2 Seguridad Informática
# Felipe Vera y Marcelo Ibarra

import hashlib


def cifrado(palabra, desplazamiento):

    # Verifica que el mensaje ingreso sea de extención n > 1
    if len(palabra) <= 1:
        return palabra

    # Desplaza las letras de la palabra según el número indicado
    mover = desplazamiento % len(palabra)
    mensaje = palabra[-mover:] + palabra[:-mover]

    # Sustituye el mensaje desplazado por letras dentro del alfabeto según el número indicado 
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    cifrado= ''
    for i in range(len(mensaje)):
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                cifrado= cifrado + alfabeto[(j+desplazamiento)%26]

                
    return(cifrado)



############################################################################################################################


# Accede al archivo de texto inicial en modo lectura
entrada = open("mensajedeentrada.txt",'r')

# Toma el contenido del archivo de texto y lo guarda dentro de la variable mensaje
mensaje = ""
for texto in entrada:
    mensaje = mensaje+texto



#Creación del primer hash
hash1 = hashlib.sha256(mensaje.encode()).hexdigest()


# Resultados
print("Mensaje de Entrada:",mensaje)
print("HASH N°1:",hash1)



# Creación del mensaje cifrado
mensajeseguro = cifrado(mensaje,3)


# Creación del archivo mensaje seguro y escritura sobre él
seguro = open("mensajeseguro.txt",'a')
seguro.write(mensajeseguro)
seguro.close()








