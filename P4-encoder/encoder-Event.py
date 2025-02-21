#!/usr/bin/env python3

############################################################
# Práctica 4 - Sensores y Actuadores
#
# Autoras: Henar Contreras y Rebeca Castilla
#
# URJC - Robótica Software
#############################################################

import RPi.GPIO as GPIO
import signal
import time
import sys
import os

# Pin
RECEPTOR = 13

# Ranuras de los dos discos
RANURAS_AZUL = 10
RANURAS_BLANCO = 20

MINUTO = 60
# Contador de ranuras por minuto
CONTADOR = 0

T0 = time.time()

def callbackSalir (senial, cuadro):
    # Ponemos este print para que '^C' quede en la siguiente linea
    print (" ")
    # Deshacemos las configuraciones
    GPIO.cleanup()
    sys.exit(0)

def callback1(canal):
    """
    Si el pin se encuentra en 1, se ha detectado un objeto.
    Comprueba si está dentro del rango
    """
    
    # Queremos que use las variables como globales,
    # no locales.
    global CONTADOR, T0, MINUTO
    
    # t será el tiempo que llevamos
    # menos el tiempo que lleva desde detectar el 'disco'
    t = time.time() - T0
    print("Tiempo: " + str(t))
    
    if GPIO.input(RECEPTOR) == GPIO.HIGH:
        os.system('clear')
        # Cada vez que detecta HIGH es que hay un objeto
        # entre el emisor y el receptor
        print("Objeto detectado")
        if t < MINUTO:
            CONTADOR = CONTADOR + 1
            print(CONTADOR)
            print("Tiempo: " + str(t))
            
        else:
            # Ya tendremos los pulsos (frecuencia) necesarios
            # para calcular la velocidad angular
            rpm(RANURAS_AZUL)
            # Reinicializamos el cronometro
            T0 = time.time()
        
    else:
        print("Ningún objeto detectado")

def rpm(ranuras, pulsos):
    """
    Utiliza una regla de tres sabiendo los pulsos (pertubaciones)
    que ha detectado el sensor en un minuto.
    
    1 rev -- Y ranuras
    rpm -- X ranuras en un minuto
    
    Y = 10
    X = CONTADOR
    
    rpm = X / Y
    """
    
    # Usamos global para cambiar el valor a CONTADOR
    global CONTADOR
    
    # Usamos una regla de tres
    revoluciones_por_minuto = ranuras / pulsos
    print("En un minuto se ha detectado la siguiente velocidad angular: " + str(revoluciones_por_minuto) + " [rpm]")
    
    # Reinicializamos el contador de ranuras por minuto
    CONTADOR = 0
    
if __name__ == '__main__':
    # Especificamos cómo vamos a tratar los puertos
    GPIO.setmode(GPIO.BOARD)
    # Configuramos los pulsadores en pull down
    GPIO.setup(RECEPTOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    # Añadimos el event para detectar cambios en el pin conectado al sensor
    GPIO.add_event_detect(RECEPTOR, GPIO.BOTH, callback=callback1, bouncetime=10)
    
    # Acabar
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()
