Práctica 4 : Ensamblador
========================
El lenguaje de maquina se especifican en dos tipos , binario y simbólico . La representación binaria es un agregado de 0 y 1 que se traduce en instrucciones de la CPU , mientras que la representación simbólica es una representación mas amigable para el programador , ya que se utilizan mnemónicos para representar las instrucciones de la CPU.La representación simbólica al no estar representando directamente en forma binaria , debe ser traducida a lenguaje de maquina para que la CPU pueda ejecutar las instrucciones , por lo cual aquí entra en juego una pieza de software llamada ensamblador , que traduce el código fuente en lenguaje ensamblador(por eso el lenguaje de maquina de manera simbólica recibe el nombre de lenguaje ensamblador) a lenguaje de maquina.<br>
En general el lenguaje ensamblador emplea los simbólos para tres propósitos:<br>
- **Etiquetas** : Se emplean para referenciar varias ubicaciones en el código , ideal para realizar estructuras de control
- **Variables** : Son nombres que se le asignan a una dirección de memoria , para poder referenciarla en el código fuente
- **Simbólos predefinidos** : Son nombres que se le asignan a valores constantes o direcciones especiales de memoria.

El ensamblador debe ser el encargado de recordar que significan cada uno de los simbolos y esta es una de sus funciones principales.<br>
Hasta este momento se ha creado la arquitectura de HACK , se ha empezado a trabajar con el lenguaje ensamblador de HACK , pero , es necesario ahondar en el proceso de construir el ensamblador que convierta el código fuente del lenguaje ensamblador de HACK a codigo de maquina para que pueda ser ejecutado por la CPU de HACK.Algo importante que se debe añadir es que el ensamblador que se realizará en esta práctica no verifica que el código realmente este correcto , el asume que el código es valido.<br>

## Explicación del Assembler

El código, realizado en Python, implementa un ensamblador que convierte instrucciones escritas en un archivo .asm a un formato binario .hack, específicamente para el conjunto de instrucciones del procesador Hack del curso "Nand to Tetris".

Para gestionar las conversiones, el ensamblador utiliza tablas de símbolos y diccionarios para almacenar instrucciones y sus correspondientes códigos binarios. El diccionario symbols asigna nombres de registros y etiquetas a direcciones de memoria específicas; por ejemplo, R0 se asocia a la dirección 0 y SCREEN a 16384. Esto permite que el ensamblador traduzca etiquetas en instrucciones a direcciones de memoria en el código binario final.

Las instrucciones se clasifican en dos tipos: tipo A y tipo C. Para las instrucciones de tipo A, el código simplemente toma un valor y lo convierte a su representación binaria de 16 bits. En cambio, para las instrucciones tipo C, el ensamblador utiliza varios diccionarios, como instructions, dest y jump, que contienen códigos binarios para diferentes operaciones. Por ejemplo, el diccionario dest especifica cómo se codifican los destinos de las operaciones, mientras que el diccionario jump se encarga de las instrucciones de salto.

El ensamblador comienza leyendo el archivo de entrada y construyendo la tabla de símbolos. En esta primera fase, se identifican etiquetas y se asignan direcciones en la memoria para ellas. Por ejemplo, una etiqueta como (LOOP) se almacenaría junto con su posición en el programa. En la segunda pasada por el archivo, el ensamblador busca instrucciones de tipo A y asigna direcciones a símbolos que aún no tienen un valor definido. Si un símbolo no es un número y no está en la tabla de símbolos, se agrega y se le asigna una dirección a partir de start_memory, comenzando en 16.

Una vez completadas las asignaciones, el ensamblador procesa nuevamente el archivo de entrada. Durante este paso, cada línea se tokeniza y convierte a su representación binaria. Las instrucciones tipo A se convierten en un formato de 16 bits, mientras que las instrucciones tipo C se construyen combinando los códigos binarios de computación, destino y salto, comenzando con un prefijo 111.

Finalmente, el código genera un archivo de salida llamado final.hack, que contiene todas las instrucciones en su formato binario. Este ensamblador no solo traduce instrucciones, sino que también proporciona una comprensión más profunda de cómo interactúan las instrucciones con el hardware a un nivel fundamental.

Lo expuesto anteriormente se puede sintetizar en la siguiente imagen:

![Assembler_Logica](https://github.com/user-attachments/assets/1a2443b7-1518-471b-b99f-65d5b99c8aff)

## Probando el assembler
### Add.asm
Tiene como objetivo realizar la suma de los valores 2 y 3, almacenando el resultado en la dirección de memoria RAM[0]. Primero, carga el valor 2 en el registro D utilizando la instrucción @2 y D=A. Luego, añade el valor 3 a lo que ya está almacenado en D con @3 y D=D+A, lo que da como resultado 5. Finalmente, el valor calculado se guarda en la posición de memoria 0 con @0 y M=D. Así, RAM[0] contiene el resultado de la suma. El programa no incluye un bucle, por lo que una vez realizada la operación, termina la ejecución. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/8f762e05-996f-487c-836e-c3cb46ce161a)

### Max.asm
Tiene como objetivo comparar los valores almacenados en las posiciones de memoria RAM[0] y RAM[1], y guardar el valor mayor en RAM[2]. El programa comienza cargando el valor de RAM[0] en el registro D (@0 y D=M). Luego, resta el valor de RAM[1] (@1 y D=D-M) para determinar cuál es mayor. Si el resultado es positivo, salta a la etiqueta OUTPUT_FIRST, lo que indica que el valor de RAM[0] es mayor. En caso contrario, carga el valor de RAM[1] y lo almacena en D. El resultado final se guarda en RAM[2], y el programa entra en un bucle infinito para detener la ejecución. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/f5259f7f-6292-437f-bfd8-081f5a9c1461)

### MaxL.asm
Esta versión del programa Max.asm se despoja de símbolos, utilizando directamente direcciones de memoria. El programa sigue el mismo proceso de comparación entre los valores de RAM[0] y RAM[1], y almacena el mayor en RAM[2]. Carga el valor de RAM[0], lo compara con el de RAM[1] restando los dos valores. Si RAM[0] es mayor, salta a la dirección donde se guarda este valor en RAM[2]; de lo contrario, almacena el valor de RAM[1]. Al final, entra en un bucle infinito, deteniendo la ejecución. Las direcciones de memoria están explícitamente definidas en lugar de utilizar etiquetas simbólicas. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/fb30fff1-7595-495e-a529-36c950c45605)

### Pong.asm
Este programa controla la pila para gestionar la ejecución de diversas instrucciones en la máquina HACK. Manipula registros como SP, ajustando la dirección actual con A=A-1 y operando sobre la memoria con M=D. El programa incluye múltiples operaciones aritméticas y de control de flujo, asegurándose de que cada valor en la pila se manipule correctamente y que el flujo del programa avance de manera coherente. A continuación, se muestra la representación simbólica y binaria del programa.
![image](https://github.com/user-attachments/assets/1ebd9529-e66d-4ce6-bb68-1a04bc09d3c1)

### PongL.asm
El archivo PongL.asm es una versión sin símbolos del código, donde se manejan directamente las direcciones numéricas para controlar el flujo del programa. El código inicializa el puntero de la pila en la dirección 256 y, a partir de ahí, realiza una serie de operaciones aritméticas y lógicas para manejar la lógica del juego. Incluye operaciones para manipular la pila, comparar valores, controlar el movimiento de la pelota, verificar colisiones y actualizar la pantalla. El código está optimizado para correr en la arquitectura Hack y sigue una estructura básica de manipulación de datos y control de flujo.

![image](https://github.com/user-attachments/assets/f6a4936a-0a6f-4e9f-8a54-b10cb95cdd06)

### Rect.asm
El archivo Rect.asm se encarga de dibujar un rectángulo en la esquina superior izquierda de la pantalla, con un ancho fijo de 16 píxeles y una altura determinada por el valor almacenado en el registro R0. El código comienza cargando el valor de R0 en un contador, que se utiliza para controlar el bucle de dibujo del rectángulo. A través de un bucle, se establece la dirección en la que se debe dibujar, y el código coloca el valor -1 en la memoria de la pantalla, representando píxeles encendidos. El bucle continúa hasta que el contador llega a cero, momento en el cual el programa entra en un bucle infinito, manteniendo el rectángulo dibujado en pantalla.
![image](https://github.com/user-attachments/assets/33de4b4a-537b-44cc-9a9a-21ec0c7cfb2b)

### RectL.asm
Tiene como objetivo dibujar un rectángulo en la máquina Hack. Inicialmente. Inicialmente, carga el valor en la dirección de memoria 0 del registro D, y si este valor es menor o igual a 0, salta al final del programa. Luego, almacena ese valor como un contador de filas en la posición de memoria 16 y guarda la dirección base de la pantalla (16384) en la posición de memoria 17, esta sirve como puntero de pantalla. A continuación, enciende un píxel en la dirección actual apuntada por 17 escribiendo -1, para posteriormente calcular la dirección de la siguiente fila sumando 32 (el ancho de la pantalla) y actualizar el puntero de pantalla. El contador de filas se decrementa en cada iteración, y si el contador es mayor que 0, el programa repite el proceso hasta completar el rectángulo. Finalmente, el programa termina cuando el contador llega a 0, deteniendo la ejecución.
![image](https://github.com/user-attachments/assets/f9a51b4f-464d-449d-8d53-b656171fa705)
