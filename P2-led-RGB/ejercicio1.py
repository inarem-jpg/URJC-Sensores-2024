###############################################
# Código programado por Henar Contreras
# y Rebeca Castilla.
#
# URJC Ingeniería de Robótica Software
#
# Sensores y Actuadores - Práctica 2
###############################################

# El import necesario para usar el modulo GPIO
import RPi.GPIO as GPIO
# Imports necesarios para usar time y funciones
# específicas de python
import time, sys

# Definimos los pines para cada color
RED_PIN = 11
BLUE_PIN = 13
GREEN_PIN = 15

def lightChange(pwmColor, valor):
    """
    Encendemos el color correspondiente al pin.
    """
    
    # Le cambiamos la intensidad
    pwmColor.ChangeDutyCycle(valor)

def cleanColors():
	"""
    Apaga los colores.
    """
    
	GPIO.output(BLUE_PIN, GPIO.HIGH)
	GPIO.output(GREEN_PIN, GPIO.HIGH)
	GPIO.output(RED_PIN, GPIO.HIGH)

def offPwm():
    """
    Desactiva los pwm
    """
    
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()
    
def primaryColor(pin):
    """
    Enciende solamente un color primario.
    """
    
    # Apagamos los colores para
    # que no se mezclen incorrectamente.
    cleanColors()
    GPIO.output(pin, GPIO.LOW)
    time.sleep(2)
    
def colorMix(redList, greenList, blueList):
    """
    Recibe una lista. Enciende los
    colores primarios que se le han pasado.
    """
    
    lightChange(redList[0], redList[1])
    lightChange(blueList[0], blueList[1])
    lightChange(greenList[0], greenList[1])
    
    time.sleep(2)
  
def rojo():
    primaryColor(RED_PIN)
    
def verde():
    primaryColor(GREEN_PIN)

def azul():
    primaryColor(BLUE_PIN)

def cyan():
    colorMix([pwmRed, 100], [pwmGreen, 0], [pwmBlue, 50])

def naranja():
    colorMix([pwmRed, 0], [pwmGreen, 50], [pwmBlue, 100])

def lima():
    colorMix([pwmRed, 50], [pwmGreen, 0], [pwmBlue, 100])
    
def lila():
    colorMix([pwmRed, 75], [pwmGreen, 75], [pwmBlue, 75])

def rosa():
    colorMix([pwmRed, 0], [pwmGreen, 100], [pwmBlue, 0])

# Indicamos que vamos a usar numeración
# de pin físico (GROUND)
GPIO.setmode(GPIO.BOARD)

# Debemos configurar los pins como salida
# para que puedan ser activados o
# desactivados por código.
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

continuar = True
while continuar:
    
    pwmRed = GPIO.PWM(RED_PIN, 100)
    pwmBlue = GPIO.PWM(BLUE_PIN, 100)
    pwmGreen = GPIO.PWM(GREEN_PIN, 100)

    print("Encendemos el rojo")
    rojo()
    print("Encendemos el verde")
    verde()
    print("Encendemos el azul")
    azul()

    pwmRed.start(100)
    pwmGreen.start(100)
    pwmBlue.start(100)

    print("Encendemos el cyan")
    cyan()
    print("Encendemos el naranja")
    naranja()
    print("Encendemos el lima")
    lima()
    print("Encendemos el lila")
    lila()
    print("Encendemos el rosa")
    rosa()
    
    offPwm()
    exiting = True
    while exiting:
        salida = input("Salir? [Y/n] ")
        if salida == "Y":
            continuar = False
            exiting = False
        elif salida == "n":
            continuar = True
            exiting = False
        else:
            print("Respuesta inesperada. Posibles respuestas: [Y, n]")

# Desactivamos el PWM
offPwm()
#Eliminamos nuestra confg de puertos
GPIO.cleanup()
