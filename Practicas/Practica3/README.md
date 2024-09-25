# Proyecto 4 : Lenguaje de Maquina 
![images](https://github.com/user-attachments/assets/1e5870d1-94ec-475b-b4fd-5dc090a3542d)


# Proyecto 5 : Arquitectura de Computadoras
En los proyectos anteriores del curso Nand2Tetris, hemos desarrollado los componentes esenciales que forman parte de la arquitectura de una computadora, tales como la ALU (Unidad Aritmético-Lógica) y la RAM (Memoria de Acceso Aleatorio). Estos bloques básicos son cruciales para ejecutar operaciones lógicas y aritméticas, además de proporcionar el almacenamiento temporal necesario durante la ejecución de programas. En este quinto proyecto, integramos todos estos módulos en una plataforma unificada conocida como la Hack Hardware Platform. Este proceso culmina con la creación de una computadora completamente funcional, capaz de ejecutar programas escritos en lenguaje de máquina Hack.

El propósito de este proyecto es completar el diseño de la CPU Hack y su plataforma de hardware. Esto requiere la interconexión de componentes clave, como la CPU, la memoria y la ROM, resultando en la creación del chip que forma el corazón de la computadora Hack. A lo largo del proyecto, veremos cómo estos componentes trabajan juntos para procesar instrucciones y manejar el flujo de datos, permitiendo que el sistema funcione de manera óptima y eficiente.

## Memory
Este código define la implementación de la memoria de la computadora Hack, incluyendo la RAM y las áreas de memoria mapeadas para el manejo de la pantalla y el teclado. La memoria es responsable de almacenar y recuperar datos durante la ejecución de un programa. Se utilizan componentes como multiplexores (Mux16) y demultiplexores (DMux) para seleccionar entre diferentes áreas de memoria dependiendo de la dirección suministrada.

![nand2tetris-mmio](https://github.com/user-attachments/assets/fb961223-9212-429b-8270-df4767b1737d)

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

El código utiliza la lógica de selección de direcciones para acceder a la RAM, la pantalla o el teclado según los bits superiores de la dirección. Esto permite que el hardware administre de manera eficiente los distintos recursos de la computadora, facilitando la interacción con el hardware externo. El diseño de la memoria en este código permite la correcta integración de la RAM y las áreas mapeadas de entrada/salida de la pantalla y teclado, formando una parte esencial del sistema de almacenamiento de la computadora Hack. La memoria no solo actúa como un área de almacenamiento de datos temporales, sino que también facilita la interacción con dispositivos externos.

## Computer
El archivo Computer.hdl define el ensamblaje completo de la computadora Hack, que incluye la CPU, la memoria y la ROM. Este chip es el componente más alto de la jerarquía, combinando todos los módulos para ejecutar programas escritos en lenguaje de máquina Hack. La CPU procesa las instrucciones almacenadas en la ROM y se comunica con la memoria para realizar las operaciones necesarias.

*Imagen*

El siguiente bloque de código muestra cómo se conectan estos componentes en la computadora Hack:
```
CHIP Computer {
    IN reset;

    PARTS:
    ROM32K(address=programCounter, out=currentInstruction);
    CPU(inM=memoryOut, instruction=currentInstruction, reset=reset, 
        outM=cpuOut, writeM=cpuWrite, addressM=cpuAddress, pc=programCounter);
    Memory(in=cpuOut, load=cpuWrite, address=cpuAddress, out=memoryOut);
}
```

En este diseño, la CPU lee las instrucciones desde la ROM, las ejecuta y escribe o lee datos en la memoria según sea necesario. El reset reinicia la ejecución del programa, lo que es útil para comenzar un nuevo ciclo de ejecución. El código Computer.hdl representa la construcción final de la computadora Hack, conectando todos los componentes principales. Este diseño asegura que la computadora Hack pueda ejecutar cualquier programa de máquina que siga las especificaciones del lenguaje Hack, demostrando cómo interactúan la CPU, la memoria y la ROM en una arquitectura simple pero funcional.

## CPU
El archivo CPU.hdl define el núcleo del sistema: la CPU (Unidad Central de Procesamiento), que contiene dos registros, A y D, una ALU (Unidad Aritmético-Lógica) y el PC (contador de programa). La CPU ejecuta las instrucciones del programa, controla el flujo de datos entre la memoria y los registros, y toma decisiones lógicas y aritméticas a través de la ALU.

*Imagen*

A continuación se muestra un fragmento del código que ilustra cómo se organiza la CPU para procesar las instrucciones y gestionar los registros:
```
CHIP CPU {
    IN  inM[16], instruction[16], reset;
    OUT outM[16], writeM, addressM[15], pc[15];

    PARTS:
    Not(in=instruction[15], out=aTypeInstruction);
    Not(in=aTypeInstruction, out=cTypeInstruction);
    And(a=cTypeInstruction, b=instruction[5], out=loadALUToA);
    Mux16(a=instruction, b=aluOutput, sel=loadALUToA, out=aRegisterInput);
    Or(a=aTypeInstruction, b=loadALUToA, out=loadARegister);
    ARegister(in=aRegisterInput, load=loadARegister, out=aRegisterOutput);

    Mux16(a=aRegisterOutput, b=inM, sel=instruction[12], out=aluYInput);
    And(a=cTypeInstruction, b=instruction[4], out=loadDRegister);
    DRegister(in=aluOutput, load=loadDRegister, out=dRegisterOutput);

    ALU(x=dRegisterOutput, y=aluYInput, zx=instruction[11], nx=instruction[10], 
        zy=instruction[9], ny=instruction[8], f=instruction[7], no=instruction[6], 
        out=aluOutput, zr=zeroFlag, ng=negativeFlag);

    Or16(a=false, b=aRegisterOutput, out[0..14]=addressM);
    Or16(a=false, b=aluOutput, out=outM);
    And(a=cTypeInstruction, b=instruction[3], out=writeM);

    And(a=zeroFlag, b=instruction[1], out=jumpIfEqual);
    And(a=negativeFlag, b=instruction[2], out=jumpIfLessThan);
    Or(a=zeroFlag, b=negativeFlag, out=zeroOrNegative);
    Not(in=zeroOrNegative, out=positiveFlag);
    And(a=positiveFlag, b=instruction[0], out=jumpIfGreaterThan);

    Or(a=jumpIfEqual, b=jumpIfLessThan, out=jumpIfLessOrEqual);
    Or(a=jumpIfLessOrEqual, b=jumpIfGreaterThan, out=jumpConditionMet);
    And(a=cTypeInstruction, b=jumpConditionMet, out=loadProgramCounter);

    Not(in=loadProgramCounter, out=incrementProgramCounter);
    PC(in=aRegisterOutput, inc=incrementProgramCounter, 
       load=loadProgramCounter, reset=reset, out[0..14]=pc);
}
```

Este código muestra cómo la CPU gestiona los registros A y D, utiliza la ALU para procesar datos y realiza saltos condicionales basados en los resultados. Los registros y la ALU trabajan en conjunto para ejecutar las instrucciones y gestionar el flujo de datos, mientras que el PC determina la próxima instrucción a ejecutar. El diseño de la CPU es el corazón de la arquitectura Hack. Su capacidad para manejar instrucciones A y C, ejecutar operaciones aritméticas y lógicas, y controlar el flujo del programa a través del PC, la convierte en el componente más crítico para ejecutar programas en esta plataforma.
