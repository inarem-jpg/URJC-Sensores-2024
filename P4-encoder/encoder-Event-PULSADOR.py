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
MINUTOS = 0

# Tiempo inicial desde que
# se detectó el objeto
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
    print("Tiempo function: " + str(t))
    
    if GPIO.input(RECEPTOR) == GPIO.LOW:
        os.system('clear')
        # Cada vez que detecta LOW es que se ha pulsado el botón
        print("Objeto detectado")
        
        if t < 60:
            CONTADOR = CONTADOR + 1
            print ("Nº de ranuras detectadas: ", CONTADOR)
        else:               
            # Ya tendremos los pulsos (frecuencia) necesarios
            # para calcular la velocidad angular
            rpm(RANURAS_AZUL, CONTADOR)
            # Reinicializamos el cronómetro
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
    revoluciones_por_minuto = (pulsos * 1) / ranuras
    print("En un minuto se ha detectado la siguiente velocidad angular: " + str(revoluciones_por_minuto) + " [rpm]")
    # Reinicializamos el contador de ranuras por minuto
    CONTADOR = 0
    
if __name__ == '__main__':
    # Especificamos cómo vamos a tratar los puertos
    GPIO.setmode(GPIO.BOARD)
    # Configuramos los pulsadores en pull up para el botón
    # porque nuestro sensor se rompió.
    # Para el encoder lo configuramos en GPIO.PUD_DOWN
    GPIO.setup(RECEPTOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    # Añadimos el event para detectar cambios en el pin conectado al sensor
    GPIO.add_event_detect(RECEPTOR, GPIO.BOTH, callback=callback1, bouncetime=10)
    
    # Acabar
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()
