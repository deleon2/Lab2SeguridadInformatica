# Universidad Finis Terrae
# Laboratorio N°2 Seguridad Informática
# Felipe Vera y Marcelo Ibarra

import hashlib

# El descifrado realiza exactamente las misma operaciones, sólo que a la inversa, todo lo que se hacia hacia la derecha,
# ahora se hace hacia la izquierda
def descifrado(palabra, desplazamiento):

    if len(palabra) <= 1:
        return palabra
    
    mover = desplazamiento % len(palabra)
    mensaje = palabra[mover:] + palabra[:mover]
    
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    cifrado= ''
    for i in range(len(mensaje)):
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                cifrado= cifrado + alfabeto[(j-desplazamiento)%26]
                
    return(cifrado)



# Lectura del archivo mensaje seguro
entrada = open("mensajeseguro.txt",'r')


# Toma el contenido del archivo de texto y lo guarda dentro de la variable mensaje
mensaje = ""

for texto in entrada:
    mensaje = mensaje+texto
entrada.close()


# Descifra el mensaje seguro
mensajedescifrado = descifrado(mensaje,3)

# Creación del segundo hash
hash2 = hashlib.sha256(mensajedescifrado.encode()).hexdigest()

# Resultados
print("Mensaje descifrado:",mensajedescifrado)
print("HASH N°2:",hash2)
