#!/usr/bin/env python3

############################################################
# Práctica 6 - Sensores y Actuadores
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

SENSOR = 23
REED = 24
LED_V = 5
LED_R = 6
LED_A = 13
LED_ALERT = 26

INFIMO = 5
SUPREMO = 20

# Variable donde guardar el tiempo
# que lleva sin detectar humedad
T = time.time()

REACTION = ' '

GPIO.setmode(GPIO.BCM)
# Debemos configurar los pins como salida
# para que puedan ser activados o
# desactivados por código
GPIO.setup(SENSOR, GPIO.OUT)
GPIO.setup(REED, GPIO.OUT)
GPIO.setup(LED_V, GPIO.OUT)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_ALERT, GPIO.OUT)

def callbackSalir (senial, cuadro):
    # Ponemos este print para que ^C quede en la siguiente linea
    print ("\n----------FIN DE REGISTRO----------")
    time.sleep(2)
    print ("\n[SHUTTING DOWN###################################]")
    # Deshacemos las configuraciones
    GPIO.cleanup()
    sys.exit(0)


def callbackHum(canal):
    """
    Comprueba el estado del reedswitch, el tiempo, y, en función de este tiempo,
    el estado al que debemos poner las LEDs.
    """

    # Queremos acceder a la reacción y cambiarle el valor
    global REACTION, T

    if GPIO.input(REED) == GPIO.LOW:
        if GPIO.input(SENSOR) == GPIO.LOW:
            print("humedad")
            stateLeds(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH)
            T = time.time()
        else:
            print("no humedad")
            # Guardamos el tiempo marcaba cuando no detectó humedad
            T = time.time()
            while time.time() - T < INFIMO:
                if (GPIO.input(SENSOR) == GPIO.LOW) or (GPIO.input(REED) == GPIO.HIGH):
                    break
                else:
                    # Si no detecta humedad, flashea la led blanca
                    # Enciende la LED verde
                    stateLeds(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW)
            else:
                while time.time() - T > INFIMO and time.time() - T < SUPREMO:
                    if (GPIO.input(SENSOR) == GPIO.LOW) or (GPIO.input(REED) == GPIO.HIGH):
                        break
                    else:
                        # Enciende la LED amarilla
                        stateLeds(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW)
                else:
                    while time.time() - T > SUPREMO:
                        if (GPIO.input(SENSOR) == GPIO.LOW) or (GPIO.input(REED) == GPIO.HIGH):
                            break
                        else:
                            # Enciende la LED roja
                            stateLeds(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW)

def stateLeds(stateV, stateR, stateA, stateAlert):
    """
    Cambia el estado de las tres LEDs.
    """

    # Estado del led verde
    GPIO.output(LED_V, stateV)
    # Estado del led rojo
    GPIO.output(LED_R, stateR)
    # Estado del led amarillo
    GPIO.output(LED_A, stateA)
    # Estado del led blanco
    GPIO.output(LED_ALERT, stateAlert)

def callbackMagnet(canal):
    """
    Si detecta que se pulsa lo enciende, de otra manera lo apaga.
    """

    # Nos interesa acceder al valor de la global
    global T, REACTION
    
    T = time.time()
    
    # Si detecta humedad, debe encender LEDs según valores de tiempo
    # de cuando NO detectó la humedad
    if GPIO.input(REED) == GPIO.LOW:
        print("Lazo cerrado")
    
    if GPIO.input(REED) == GPIO.HIGH:
        print("Reed en lazo abierto")
        stateLeds(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW)
        
if __name__ == '__main__':
    # Configuramos los pulsadores en pull up
    GPIO.setup(REED, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    print("[VOZ DE IA] Bienvenido a nuestro sistema\nde control en base a la humedad.")
    time.sleep(2)
    print("En nuestra base de datos tenemos acceso\n a las siguientes librerías:\n")
    time.sleep(2)
    print("--------------------------------------------")
    print("*Doble click para seleccionar librería*\n")
    print("--------------------------------------------")
    time.sleep(2)
    print("[DISPLAY INDEX]\n")
    time.sleep(2)
    print("Para la librería seleccionada, se\n implementarán especificaciones")
    print("de cuidado.")
    time.sleep(2)
    # No hemos implementado verificacion de Y/n 
    # porque no era el objetivo de la práctica
    input("¿Está seguro de querer proceder?")
    time.sleep(2)
    print("\n[LOADING###################################]\n\n")
    time.sleep(3)
    print("----------REGISTRO DE PROGRAMA----------")
    # Añadimos el event de detectar cualquier edge (R/F) en el reedswitch
    GPIO.add_event_detect(REED, GPIO.BOTH, 
      callback=callbackMagnet, bouncetime=200)
    # Añadimos el event de detectar cualquier edge (R/F) en el sensor de humedad
    GPIO.add_event_detect(SENSOR, GPIO.BOTH, 
      callback=callbackHum, bouncetime=200)
      
    # Acabar
    signal.signal(signal.SIGINT, callbackSalir)
    signal.pause()
