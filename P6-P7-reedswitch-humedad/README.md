# P6-7 ReedSwitch y Humedad

## Details
Fecha: 14/12/2024.

Autoras: Castilla Puerta, Rebeca y Contreras Mateos, Henar.

Objetivo: Implementación de reedswitch con sensor de humedad y diferentes LEDs.

Disclaimer: El código tiene pensado poder ser un borrador para un proyecto hipotético
 enfocado a la domótica para el cuidado de ciertas familias de objetos que dependan 
de tener estar húmedos o no. Como no tenemos ni una base de datos de estas máquinas 
que gestionar, ni estamos enfocadas en la búsqueda por algoritmos de estos objetos,
 hemos añadidos prints demo de esta posible interacción usuario-programa.
De una misma manera, el tiempo de los rangos debería gestionarse dependiendo de 
estas librerías.

Resumen: Contiene un código en el que primero se espera a que el reedswitch esté
 en lazo cerrado. Luego, en función de unos valores de tiempo y de si capta humedad
 o no, enciende tres LEDs: verde, amarilla o roja. 

Los rangos de segundos pues, quedan de esta manera:
  - verde [0, 5]
  - amarillo (5, 20]
  - rojo (t > 20)

En la vida real probablemente en vez de segundos, los tiempos serían horas.
Hay dos versiones de la practica, la versión 1.1 es más rudimentaria y enciende 
los LEDS una vez ha detectado la humedad, con el tiempo que ha contado cuando no 
la detectaba. Es decir, cuando no detecta humedad empieza un contador, con los 
parámetros de colores previamente especificados, y una vez se detecta la humedad, 
enciende el LED del tiempo correspondiente a cuanto estuvo sin humedad.

La versión 1.2 enciende el LED mientras NO detecta humedad. Nada más no detecta 
humedad, enciende un LED verde, a los 5 segundos de no detectarlo amarillo y a 
los 20 hasta que detecta humedad, rojo; una vez detecta humedad enciende el LED 
blanco y reinicia el contador.

También hemos incluido dos códigos en los que el sensor de humedad y el reed 
switch encienden una LED cuando detectan cosas individualmente 
(event-reed.py y event-hum.py).


Este es el video de la versión 1.1:

https://github.com/user-attachments/assets/6a6f79f6-6b09-448f-9295-ce10aa456ae6

Este es el video de la versión 1.2:

https://github.com/user-attachments/assets/81ba9380-cf4d-41e5-9147-3289f0c87bff
