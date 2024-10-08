# Proyecto 4 : Lenguaje de Maquina 
En este momento del proyecto , se han abordado la construcción de chips para memoria y procesamiento , antes de pasar a la construcción o ensamblaje de la arquitectura de HACK , se hace necesario abordar el lenguaje de maquina , ya que una computadora de proposito general debe ser capaz de ejecutar cualquier programa escrito en lenguaje de maquina.Un lenguaje de máquina es un formalismo acordado diseñado para codificar instrucciones de la máquina. Usando estas instrucciones, podemos instruir al procesador de la computadora para realizar operaciones aritméticas y lógicas, leer y escribir valores desde y hacia la memoria de la computadora, probar condiciones booleanas, y decidir qué instrucción buscar y ejecutar a continuación. Tambien se destaca que con el lenguaje de maquina tenemos algo denominado *lenguaje de bajo nivel* por lo cual estamos interactuando directamente (o de cierta manera) con el hardware de la computadora.<br>
El lenguaje de maquina en principio solo era posible escribirse de manera binaria , siendo algo muy complejo ya que se debian representar instrucciones mediante ciertos numeros binarios , por lo cual se desarrollo una manera simbólica de escribir lenguaje de maquina , a este nuevo lenguaje se le denomino *lenguaje ensamblador* ademas de ser mas facil de escribir y leer permitiendo tener contacto con la ALU , memorias y registros de manera mas sencilla, tambien es mas facil de traducir a lenguaje de maquina usando una pieza de software llamada *ensamblador*.<br>Algo a destacar sobre el lenguaje ensamblador es que al estar muy ligado a los detalles de bajo nivel del hardware,no existe un unico consenso sobre la sintaxis del lenguaje ensamblador.Específicamente el vinculo entre la arquitectura del computador y el lenguaje ensamblador es intrínseco ya que cada procesador o familia de procesadores tiene su propio conjunto de instrucciones (*ISA*) por lo cual el lenguaje ensamblador debe adecuarse a este Los procesadores diferentes, como x86, ARM, MIPS, o el procesador Hack (en el proyecto Nand2Tetris), tienen conjuntos de instrucciones distintos.Los procesadores diferentes, como x86, ARM, MIPS, o el procesador de Hack (en el proyecto Nand2Tetris), tienen conjuntos de instrucciones distintos,entonces el *ISA* define las operaciones que un procesador puede realizar, como mover datos entre registros, sumar, multiplicar, o hacer saltos condicionales. Por ejemplo, en x86 hay instrucciones como MOV, ADD, y JMP, mientras que en un procesador ARM, las instrucciones son diferentes aunque puedan cumplir funciones similares.<br>
A continuación se presentara un breve resumen sobre el lenguaje ensamblador y su implementación en el proyecto Nand2Tetris:<br>

1. Arquitectura de HACK

    El procesador Hack es una CPU simplificada con tres registros principales:
    - A: Registro de direcciones (también utilizado para datos en ciertas ocasiones).
    - D: Registro de datos.
    - M: Valor en la dirección de memoria apuntada por el registro A.

    La memoria tiene 32K palabras, con un mapeo de memoria donde se representan tanto los datos como los componentes de entrada/salida, como el teclado y la pantalla.

Las instrucciones de Hack se dividen en dos categorías: A-instructions y C-instructions.

2. A-Instructions
    Las A-instructions establecen el valor del registro A con un número o una etiqueta que apunta a una dirección de memoria.
    Sintaxis: @value
    - @number: Carga el valor numérico en el registro A.
    - @label: Apunta a una etiqueta que corresponde a una dirección de memoria.

    Ejemplo: @17 asigna el valor 17 al registro A.

Efectos:
    Se selecciona la dirección de memoria para futuras operaciones (cuando se usa M).
    Se puede utilizar en operaciones de salto (cuando se usa con instrucciones condicionales).

3. C-Instructions
    Las C-instructions son más complejas y están destinadas a operaciones de la ALU (Unidad Aritmético-Lógica), movimientos de datos entre registros y saltos condicionales.
    La sintaxis de una C-instruction sigue el formato: dest = comp ; jump.
    - comp: Especifica la operación que realizará la ALU.
    - dest: Indica dónde almacenar el resultado (A, D, M o una combinación de ellos).
    - jump: Controla si debe realizarse un salto condicional basado en el resultado del cómputo.

Ejemplos:
- D = A + 1: Incrementa el valor de A en 1 y lo guarda en D.
- 0;JMP: Salta incondicionalmente a la dirección en el registro A.
- D;JEQ: Salta si el valor en D es igual a cero.

4. Símbolos y Etiquetas
    El lenguaje ensamblador Hack permite definir etiquetas que facilitan el control del flujo del programa. Las etiquetas son identificadores que marcan una dirección de memoria y se usan con instrucciones de salto.A continuación se muestra un ejemplo :
    ```
    (LOOP)
    .
    .
    .
    @LOOP
    D;JEQ
    . rest of the program
    ```
    se declara una equiqueta LOOP y se salta otra vez a ella si el registro de datos D es igual a 0.
En la siguiente gráfico se puede apreciar el conjunto de instrucciones completos del lenguaje ensamblador de HACK : <br>
<img src="https://github.com/user-attachments/assets/a1c136d1-143e-4307-b0e4-76d95b3a430d" width="400" height="350" text-align="center"/>
<br>
Para este proyecto se tenia el objetivo que se adquiera una idea de la programación de bajo nivel y concer a profundidas el sistema informático Hack.Esto se hizo escribiendo y ejecutando dos programas de bajo nivel, escritos en el lenguaje ensamblador Hack.El primero de ellos consistia en realizar un programa de multiplicar dos números alojados en 2 registros diferentes , mientras que el segundo a partir de detectar el evento de presionar una tecla del teclado empezar a llenar la pantalla con un patrón que se desease esto mediante el cambio de cada pixel a un color negro y si se dejaba de presionar dicho patrón se iba borrando progresivamente ya que los pixeles se cambiarian a color blanco: <br>
<img src="https://github.com/user-attachments/assets/9048f5ff-6ccc-4fc2-89d4-fbd4333c20d1" width="400" height="350" text-align="center"/>

# Proyecto 5 : Arquitectura de Computadoras
En los proyectos anteriores del curso Nand2Tetris, hemos desarrollado los componentes esenciales que forman parte de la arquitectura de una computadora, tales como la ALU (Unidad Aritmético-Lógica) y la RAM (Memoria de Acceso Aleatorio). Estos bloques básicos son cruciales para ejecutar operaciones lógicas y aritméticas, además de proporcionar el almacenamiento temporal necesario durante la ejecución de programas. En este quinto proyecto, integramos todos estos módulos en una plataforma unificada conocida como la Hack Hardware Platform. Este proceso culmina con la creación de una computadora completamente funcional, capaz de ejecutar programas escritos en lenguaje de máquina Hack.

El propósito de este proyecto es completar el diseño de la CPU Hack y su plataforma de hardware. Esto requiere la interconexión de componentes clave, como la CPU, la memoria y la ROM, resultando en la creación del chip que forma el corazón de la computadora Hack. A lo largo del proyecto, veremos cómo estos componentes trabajan juntos para procesar instrucciones y manejar el flujo de datos, permitiendo que el sistema funcione de manera óptima y eficiente.

## Memory
Este código define la implementación de la memoria de la computadora Hack, incluyendo la RAM y las áreas de memoria mapeadas para el manejo de la pantalla y el teclado. La memoria es responsable de almacenar y recuperar datos durante la ejecución de un programa. Se utilizan componentes como multiplexores (Mux16) y demultiplexores (DMux) para seleccionar entre diferentes áreas de memoria dependiendo de la dirección suministrada.

![Memory](https://github.com/user-attachments/assets/fb961223-9212-429b-8270-df4767b1737d)

El siguiente bloque de código muestra cómo se organiza la memoria en función de las direcciones, cargando la RAM o los mapas de memoria de pantalla y teclado según corresponda:
```
CHIP Memory {
    IN in[16], load, address[15];
    OUT out[16];

    PARTS:
    // Demultiplexa la señal de carga entre las diferentes memorias según las líneas de dirección más altas
    DMux4Way(in=load, sel=address[13..14], a=loadToRAM1, b=loadToRAM2, c=loadToScreen, d=loadToKeyboard);
    
    // Combinamos las señales para cargar en la RAM de 16K si alguna de las primeras dos opciones es seleccionada
    Or(a=loadToRAM1, b=loadToRAM2, out=loadToRAM);

    // RAM de 16K respondiendo a las primeras 14 líneas de dirección
    RAM16K(in=in, load=loadToRAM, address=address[0..13], out=outputFromRAM);

    // La pantalla usa menos líneas de dirección y tiene su propia señal de carga
    Screen(in=in, load=loadToScreen, address=address[0..12], out=outputFromScreen);

    // El teclado no tiene líneas de entrada o de carga, simplemente proporciona su estado actual
    Keyboard(out=outputFromKeyboard);

    // Selecciona la salida correcta basada en las líneas de dirección altas
    Mux4Way16(a=outputFromRAM, b=outputFromRAM, c=outputFromScreen, d=outputFromKeyboard, sel=address[13..14], out=out);
}
```

El código utiliza la lógica de selección de direcciones para acceder a la RAM, la pantalla o el teclado según los bits superiores de la dirección. Esto permite que el hardware administre de manera eficiente los distintos recursos de la computadora, facilitando la interacción con el hardware externo. El diseño de la memoria en este código permite la correcta integración de la RAM y las áreas mapeadas de entrada/salida de la pantalla y teclado, formando una parte esencial del sistema de almacenamiento de la computadora Hack. La memoria no solo actúa como un área de almacenamiento de datos temporales, sino que también facilita 
a interacción con dispositivos externos.

l![Resultado](https://github.com/user-attachments/assets/f6943dd8-dd9a-45da-b032-9bfc0a10aa38)

## CPU
El archivo CPU.hdl define el núcleo del sistema: la CPU (Unidad Central de Procesamiento), que contiene dos registros, A y D, una ALU (Unidad Aritmético-Lógica) y el PC (contador de programa). La CPU ejecuta las instrucciones del programa, controla el flujo de datos entre la memoria y los registros, y toma decisiones lógicas y aritméticas a través de la ALU.

![CPU](https://github.com/user-attachments/assets/6f581084-d0f6-4fb1-bfc2-c3468d01d131)


A continuación se muestra un fragmento del código que ilustra cómo se organiza la CPU para procesar las instrucciones y gestionar los registros:
```
CHIP CPU {

    IN  inM[16],         // Entrada del valor de M (M = contenido de RAM[A])
        instruction[16], // Instrucción a ejecutar
        reset;           // Señal para reiniciar el programa actual (reset == 1)
                         // o continuar ejecutando el programa actual (reset == 0).

    OUT outM[16],        // Salida del valor de M
        writeM,          // ¿Escribir en M?
        addressM[15],    // Dirección de RAM (de M)
        pc[15];          // Dirección de ROM (de la próxima instrucción)

    PARTS:
    // Determina el tipo de instrucción
    Not(in=instruction[15], out=instA);
    Not(in=instA, out=instC);
    
    And(a=instC, b=instruction[5], out=dirAfromALU);    // ¿Instrucción C y destino al registro A?
    Mux16(a=instruction, b=aluOut, sel=dirAfromALU, out=regAin);
    
    Or(a=instA, b=dirAfromALU, out=loadAreg);    // Carga A si inst de tipo A o C con destino a A
    ARegister(in=regAin, load=loadAreg, out=Aout);
    
    Mux16(a=Aout, b=inM, sel=instruction[12], out=AMout);   // Selecciona A o M basado en el bit 'a'

    And(a=instC, b=instruction[4], out=loadDreg);
    DRegister(in=aluOut, load=loadDreg, out=Dout);    // Carga el registro D desde la ALU
    
    ALU(x=Dout, y=AMout, zx=instruction[11], nx=instruction[10], 
        zy=instruction[9], ny=instruction[8], f=instruction[7],
        no=instruction[6], out=aluOut, zr=zrOut, ng=ngOut); // Calcula operación ALU
        
    // Configura salidas para escribir en memoria
    Or16(a=false, b=Aout, out[0..14]=addressM);
    Or16(a=false, b=aluOut, out=outM);
    And(a=instC, b=instruction[3], out=writeM);
    
    // Calcula condiciones de salto y carga del PC
    And(a=zrOut, b=instruction[1], out=jumpEqual);    // Es cero y salta si es cero
    And(a=ngOut, b=instruction[2], out=jumpLessThan);    // Es negativo y salta si es negativo
    Or(a=zrOut, b=ngOut, out=zeroOrNeg);
    Not(in=zeroOrNeg, out=positive);            // Es positivo (no cero ni negativo)
    And(a=positive, b=instruction[0], out=jumpGreaterThan); // Es positivo y salta si es positivo
    Or(a=jumpEqual, b=jumpLessThan, out=jumpLessEqual);
    Or(a=jumpLessEqual, b=jumpGreaterThan, out=jumpToA);    // Carga PC si se cumple condición de salto
    And(a=instC, b=jumpToA, out=loadPC); // Solo salta si es instrucción C
    Not(in=loadPC, out=incPC);                  // Solo incrementa si no se carga
    PC(in=Aout, inc=incPC, load=loadPC, reset=reset, out[0..14]=pc);
}
```

Este código muestra cómo la CPU gestiona los registros A y D, utiliza la ALU para procesar datos y realiza saltos condicionales basados en los resultados. Los registros y la ALU trabajan en conjunto para ejecutar las instrucciones y gestionar el flujo de datos, mientras que el PC determina la próxima instrucción a ejecutar. El diseño de la CPU es el corazón de la arquitectura Hack. Su capacidad para manejar instrucciones A y C, ejecutar operaciones aritméticas y lógicas, y controlar el flujo del programa a través del PC, la convierte en el componente más crítico para ejecutar programas en esta plataforma.

## Computer
El archivo Computer.hdl define el ensamblaje completo de la computadora Hack, que incluye la CPU, la memoria y la ROM. Este chip es el componente más alto de la jerarquía, combinando todos los módulos para ejecutar programas escritos en lenguaje de máquina Hack. La CPU procesa las instrucciones almacenadas en la ROM y se comunica con la memoria para realizar las operaciones necesarias.

![Computer](https://github.com/user-attachments/assets/9a5b5166-7a41-424f-a749-1e69e4aebd30)

El siguiente bloque de código muestra cómo se conectan estos componentes en la computadora Hack:
```
CHIP Computer {

    IN reset;  // Señal de reinicio para el computador

    PARTS:
    // La unidad de memoria de solo lectura (ROM) almacena el programa a ejecutar
    ROM32K(address=pc, out=instruction);
    
    // La unidad central de procesamiento (CPU) ejecuta las instrucciones
    CPU(inM=dataFromMemory, instruction=instruction, reset=reset, 
        outM=dataToMemory, writeM=signalWriteM, addressM=memoryAddress, pc=pc);
    
    // La memoria principal que interactúa con la CPU para almacenar y recuperar datos
    Memory(in=dataToMemory, load=signalWriteM, address=memoryAddress, out=dataFromMemory);
}

```

En este diseño, la CPU lee las instrucciones desde la ROM, las ejecuta y escribe o lee datos en la memoria según sea necesario. El reset reinicia la ejecución del programa, lo que es útil para comenzar un nuevo ciclo de ejecución. El código Computer.hdl representa la construcción final de la computadora Hack, conectando todos los componentes principales. Este diseño asegura que la computadora Hack pueda ejecutar cualquier programa de máquina que siga las especificaciones del lenguaje Hack, demostrando cómo interactúan la CPU, la memoria y la ROM en una arquitectura simple pero funcional.

![Salida](https://github.com/user-attachments/assets/65995869-db4b-4890-99be-353486f8d0ad)
