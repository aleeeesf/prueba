import socket #constructor socket
import os     # Modulo de funcionalidades dependientes del sistema operativo

HOST = '192.168.0.10' #host utilizado
PORT = 8008 #puerto utilizado

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# Seleccionamos el tipo y familia de socket en este caso para UDP

s_udp.sendto('Soy el cliente'.encode(), (HOST, PORT)) #Enviamos un mensaje al servidor

s_udp.close() #cerramos la comunicación
