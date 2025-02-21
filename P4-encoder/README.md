# P4-Encoder
**Fecha**: 27/11/2024.

**Autoras**: Castilla Puerta, Rebeca y Contreras Mateos, Henar.

**Objetivo**: Cálculo de rpm de un disco conectado a un motor mediante un encoder

**Resumen**: Una mitad del encoder es un transistor, la otra mitad, un fotodiodo, 
  los cuales se mandan información continuamente cuando nada se encuentra entre
  la ranura del encoder; cuando un objeto se encuentra entre las dos mitades,
  se para la transmisión.

  Hemos encontrado varios problemas con la práctica, con el optointerruptor 
  específicamente, el grupo de Miguel ha descubierto que estos se pueden
  desconfigurar cuando se acercan a un motor, causando que no detecten bien
  los flancos de subida y bajada, que es exactamente lo que nos ha pasado a 
  nosotras.

  La semana anterior a la entrega, el código y el circuito funcionaban, pero 
  llegado el dia de la entrega (cómo no), pese a estar el circuito y el código 
  igual, de repente no funcionaba el optointerruptor, creemos que por esta 
  desconfiguración (ya que varios compañeros más han tenido este programa)

  Por esto, hemos modificado ligeramente el código del encoder para que funcione
  con un pulsador (cuya funcionalidad es básicamente la misma), adjuntamos ambos
  códigos en la práctica, y ponemos aquí las diferencias:

En el pulsador:
```
if GPIO.input(RECEPTOR) == GPIO.LOW:
```
```
GPIO.setup(RECEPTOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
``` 
vs. en el optointerruptor:
```
if GPIO.input(RECEPTOR) == GPIO.HIGH:
```
```
GPIO.setup(RECEPTOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
```
  Tenemos dos variable para calcular las revoluciones, RANURAS_AZUL y 
  RANURAS_BLANCO, que se corresponden con las dos ruedas que tenemos, la azul 
  con 10 ranuras y la blanca con 20 (en el código usamos la azul de ejemplo,
  pero bastaría cambiarle el nombre y calcularía las revoluciones con el nº de 
  ranuras de la otra rueda)
  
  Para calcular las rpm hemos hecho una regla de tres; hemos tenido en cuenta
  que en una revolución se deberían detectar Y ranuras (variables definidas al 
  inicio, las nuestras RANURAS_AZUL y RANURAS_BLANCO) y que para las revoluciones 
  por minuto detectará ese número de ranuras por el número de vueltas dadas. 
  Nosotras contamos directamente el número de ranuras totales detectadas en 60 
  segundos, y lo dividimos entre el número de ranuras iniciales.
  
  Foto del circuito con el encoder:

  
![WhatsApp Image 2024-11-27 at 5 48 16 PM](https://github.com/user-attachments/assets/4c1c0a9f-05b7-481f-b5ce-875f10a12a92)
  
![WhatsApp Image 2024-11-27 at 5 48 15 PM](https://github.com/user-attachments/assets/d5e723a2-c871-4569-9e40-9a94aa2cc884)

  Video del código (usando el pulsador)
  
  https://github.com/user-attachments/assets/e8a24ccc-42f4-48cc-8454-6b7d1badd577


