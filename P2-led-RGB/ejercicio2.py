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

# Lista de colores predeterminados
LISTA_COLORES_IMPLEMENTADOS = ["cyan", "rojo", "azul", "verde", "rosa", "lima", "naranja", "lila"]

# Indicamos que vamos a usar numeración
# de pin físico (GROUND)
GPIO.setmode(GPIO.BOARD)

# Debemos configurar los pins como salida
# para que puedan ser activados o
# desactivados por código.
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

pwmRed = GPIO.PWM(RED_PIN, 100)
pwmBlue = GPIO.PWM(BLUE_PIN, 100)
pwmGreen = GPIO.PWM(GREEN_PIN, 100)

def usage():
    
    usage = """
        usage
            Devuelve este mensaje
        colores
            Enseña una lista de colores predeterminados
        encender [color]
            Enciende color
        apagar [color]
            Apaga color
        mix [-n | valor1 valor2 valor3] (valores entre 0.0 y 100.0)
            Valores entre 0.0 y 100.0.
            Muestra un color personalizado o lo apaga [-n]
        salir
            Termina el programa
    """
    
    print(usage)
    
def lightChange(pwmColor, valor):
    """
    Encendemos el color correspondiente al pin.
    """
    
    # Le cambiamos la intensidad
    pwmColor.ChangeDutyCycle(valor)

def cleanColors():
	"""
    Desactiva los pines.
    """
    
	GPIO.output(BLUE_PIN, GPIO.HIGH)
	GPIO.output(GREEN_PIN, GPIO.HIGH)
	GPIO.output(RED_PIN, GPIO.HIGH)

def offPwm():
    """
    Interrumpe los pwm de cada pin.
    """
    
    pwmRed.stop()
    pwmGreen.stop()
    pwmBlue.stop()

def onPwm():
    """
    Configura los pines para poder usar los pwm
    e inicializa los ciclos.
    """
    
    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(BLUE_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    
    # En ánodo 100 apaga
    pwmRed.start(100)
    pwmGreen.start(100)
    pwmBlue.start(100)

def colorMix(redList, greenList, blueList):
    """
    Recibe una lista. Enciende los
    colores primarios que se le han pasado.
    """
    
    #Activamos los ciclos
    onPwm()
    # Asignamos valores a cada pwm.
    lightChange(redList[0], redList[1])
    lightChange(greenList[0], greenList[1])
    lightChange(blueList[0], blueList[1])
    
    time.sleep(2)

def colores():
    """
    Imprime la lista de colores implementados.
    """
    
    print(LISTA_COLORES_IMPLEMENTADOS)
    
def rojo():
    """
    Enciende el color primario rojo.
    """
    
    colorMix([pwmRed, 0], [pwmGreen, 100], [pwmBlue, 100])
    
def verde():
    """
    Enciende el color primario verde.
    """

    colorMix([pwmRed, 100], [pwmGreen, 0], [pwmBlue, 100])

def azul():
    """
    Enciende el color primario azul.
    """

    colorMix([pwmRed, 100], [pwmGreen, 100], [pwmBlue, 0])

def cyan():
    """
    Guarda los valores que le vamos a pasar al pwm.
    Llama a otra función para generar el cyan.
    
    Se le pasa el pwm de cada color primario
    y el valor guardado en storage que queremos.
    """
    
    colorMix([pwmRed, 100], [pwmGreen, 0], [pwmBlue, 50])

def naranja():
    """
    Guarda los valores que le vamos a pasar al pwm.
    Llama a otra función para generar el naranja.

    Se le pasa el pwm de cada color primario
    y el valor guardado en storage que queremos.
    """
    
    colorMix([pwmRed, 0], [pwmGreen, 50], [pwmBlue, 100])

def lima():
    """
    Guarda los valores que le vamos a pasar al pwm.
    Llama a otra función para generar el lima.
    
    Se le pasa el pwm de cada color primario
    y el valor guardado en storage que queremos.
    """

    colorMix([pwmRed, 50], [pwmGreen, 0], [pwmBlue, 100])
    
def lila():
    """
    Guarda los valores que le vamos a pasar al pwm.
    Llama a otra función para generar el lila.
    
    Se le pasa el pwm de cada color primario
    y el valor guardado en storage que queremos.
    """
    
    colorMix([pwmRed, 75], [pwmGreen, 75], [pwmBlue, 75])

def rosa():
    """
    Guarda los valores que le vamos a pasar al pwm.
    Llama a otra función para generar el rosa.
    
    Se le pasa el pwm de cada color primario
    y el valor guardado en storage que queremos.
    """
    
    colorMix([pwmRed, 0], [pwmGreen, 100], [pwmBlue, 0])

def inversa(función):
    """
    La función de apagado.
    
    Busca cuándo se ha mandado apagar un color
    primario y manda que el pin se apague directamente.

    De otra manera, habría que apagar el ciclo de trabajo
    porque en los otros colores se están usando los pwm.
    """

    offPwm()
    GPIO.cleanup()
          
# Guardamos un diccionario para poder ejecutar las funciones asignadas a un string de mismo nombre de manera más sencilla
DICT_COLORES = {"cyan": cyan, "rojo": rojo, "azul": azul, "verde":verde , "rosa": rosa, "lima": lima, "naranja": naranja, "lila": lila}

def ordenColor(orden, color):
    
    # Le quitamos 1 porque el índice de la lista empieza en 0
    n = len(LISTA_COLORES_IMPLEMENTADOS)
    
    colorUsar = False
    for i in range(n):
        # Si el color es uno de los predeterminados
        if  color == LISTA_COLORES_IMPLEMENTADOS[i]:
            colorUsar = True
            break
        
        # En el último elemento sabremos si es un color incorrecto
        if i == (n - 1):
            if color != LISTA_COLORES_IMPLEMENTADOS[i]:
                print("Color incorrecto.\n")
                print(LISTA_COLORES_IMPLEMENTADOS)
                print("Usa estos colores o utiliza la función mix\n")
            
                colorUsar = False
            
    if colorUsar:
        if orden == "encender":
            # Ejecuta la función
            DICT_COLORES[color]()
        elif orden == "apagar":
            # Apaga la LED o los pwm en función del color
            inversa(DICT_COLORES[color])
        
print("Bienvenid@")
print("\nCon nuestro código podrás encender o apagar la siguiente LED RGB")
print("para 8 colores diferentes, además de poder crear otros colores a través de diferentes valores.")
print("\nFunciones:")
usage()

onPwm()

ejecutar = True
while ejecutar:
    # Indicamos que vamos a usar numeración
    # de pin físico (GROUND)
    GPIO.setmode(GPIO.BOARD)
    
    orderString = input("Orden a ejecutar... ")
    lista = orderString.split()
    
    n = len(lista)
    
    # Comprueba el número de elementos
    if n < 1 or n > 5 or n == 3:
        print("Número de argumentos incorrecto.")
        time.sleep(1)
        usage()
    
    if n == 1:
        if orderString == "usage":
            usage()
        elif orderString == "colores":
            # Imprime la lista de colores predeterminados
            colores()
        elif orderString == "salir":
            ejecutar = False
        else:
            print("Uso incorrecto")
            usage()
        
    elif n == 2:
        if lista[0] == "encender":
            # Le pasa encender y el color
            ordenColor(lista[0], lista[1])
        elif lista[0] == "apagar":
            # Le pasa apagar y el color
            ordenColor(lista[0], lista[1])
        elif lista[1] == "-n":
            offPwm()
            GPIO.cleanup()
        else:
            print("Uso incorrecto")
            usage()
        
    elif n == 4:
        colorMix([pwmRed, float(lista[1])], [pwmGreen, float(lista[2])], [pwmBlue, float(lista[3])])
    
# Desactivamos el PWM
offPwm()
#Eliminamos nuestra confg de puertos
GPIO.cleanup()
