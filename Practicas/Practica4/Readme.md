Práctica 4 : Ensamblador
========================
El lenguaje de maquina se especifican en dos tipos , binario y simbólico . La representación binaria es un agregado de 0 y 1 que se traduce en instrucciones de la CPU , mientras que la representación simbólica es una representación mas amigable para el programador , ya que se utilizan mnemónicos para representar las instrucciones de la CPU.La representación simbólica al no estar representando directamente en forma binaria , debe ser traducida a lenguaje de maquina para que la CPU pueda ejecutar las instrucciones , por lo cual aquí entra en juego una pieza de software llamada ensamblador , que traduce el código fuente en lenguaje ensamblador(por eso el lenguaje de maquina de manera simbólica recibe el nombre de lenguaje ensamblador) a lenguaje de maquina.<br>
En general el lenguaje ensamblador emplea los simbólos para tres propósitos:<br>
- **Etiquetas** : Se emplean para referenciar varias ubicaciones en el código , ideal para realizar estructuras de control
- **Variables** : Son nombres que se le asignan a una dirección de memoria , para poder referenciarla en el código fuente
- **Simbólos predefinidos** : Son nombres que se le asignan a valores constantes o direcciones especiales de memoria.

El ensamblador debe ser el encargado de recordar que significan cada uno de los simbolos y esta es una de sus funciones principales.<br>
Hasta este momento se ha creado la arquitectura de HACK , se ha empezado a trabajar con el lenguaje ensamblador de HACK , pero , es necesario ahondar en el proceso de construir el ensamblador que convierta el código fuente del lenguaje ensamblador de HACK a codigo de maquina para que pueda ser ejecutado por la CPU de HACK.Algo importante que se debe añadir es que el ensamblador que se realizará en esta práctica no verifica que el código realmente este correcto , el asume que el código es valido.<br>

## Probando el assembler
### Add.asm
Las pruebas en add.asm mostraron la suma de 2 y 3, almacenando el resultado en RAM[0]. El ensamblador traduce las instrucciones simbólicas a código binario para ser ejecutadas por la CPU HACK. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/8f762e05-996f-487c-836e-c3cb46ce161a)

### Max.asm
Las pruebas del ensamblador para Max.asm mostraron cómo se calcula el valor máximo entre R0 y R1, almacenando el resultado en R2. El ensamblador traduce las instrucciones simbólicas que comparan estos registros y asigna el mayor valor en código binario para su ejecución en la CPU HACK. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/f5259f7f-6292-437f-bfd8-081f5a9c1461)

### MaxL.asm
Las pruebas del ensamblador para MaxL.asm mostraron la versión sin símbolos del programa Max.asm, diseñada para probar la versión básica del ensamblador. Este programa compara los valores de dos registros y almacena el mayor sin el uso de etiquetas o variables simbólicas, con todas las direcciones de memoria especificadas directamente. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/fb30fff1-7595-495e-a529-36c950c45605)

### Pong.asm
Las pruebas del ensamblador para Pong.asm muestran cómo se manipulan registros de memoria y la pila (SP) usando instrucciones como @SP y A=A-1. El panel izquierdo contiene el código simbólico, y el central su traducción binaria. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/1ebd9529-e66d-4ce6-bb68-1a04bc09d3c1)

### PongL.asm
![image](https://github.com/user-attachments/assets/f6a4936a-0a6f-4e9f-8a54-b10cb95cdd06)

### Rect.asm
![image](https://github.com/user-attachments/assets/33de4b4a-537b-44cc-9a9a-21ec0c7cfb2b)

### RectL.asm
![image](https://github.com/user-attachments/assets/f9a51b4f-464d-449d-8d53-b656171fa705)



