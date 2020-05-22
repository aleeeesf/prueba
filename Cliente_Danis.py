import socket #constructor socket
import os # Modulo de funcionalidades dependientes del sistema operativo

HOST = 'localhost' #host utilizado
PORT = 1025 #puerto utilizado

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Seleccionamos el tipo y familia de socket en este caso para TCP
s.connect((HOST,PORT)) #enlazamos el host con los puertos

s.send(bytes("Hola servidor","utf-8")) #enviamos mensaje al servidor

mensaje = s.recv(1024) #recibimos el mensaje
print(mensaje.decode("utf-8")) #imprimimos el mensaje del servidor por pantalla


print("Hola, he añadido esta linea")
s.close()
