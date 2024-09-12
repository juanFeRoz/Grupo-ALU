# Proyecto 2 : Aritmética Booleana
La *CPU* (Central Processing Unit) es aquella que puede ejecutar cualquier instrucción que pueda manejar una computadora. Como pieza central de esta unidad, se encuentra la *ALU* (Arithmetic Logic Unit). La ALU es la encargada de realizar las operaciones lógicas y aritméticas que requiera la arquitectura de la computadora.
El proyecto 2 se dirige a la construcción de una ALU llamada *HACK*, a partir de las compuertas lógicas del proyecto 1. Como objetivo principal, *HACK* operará sobre 2 entradas de 16 bits, logrando realizar 18 funciones (en realidad puede realizar hasta 64, pero se enfocará en tan solo ese número) en base a 6 entradas de 1 bit de control.
Para la implementación de *HACK*, se emplearon 3 elementos principales: multiplexores de 16 bits, sumador completo de 16 bits, negación y conjunción para 16 bits. Se hace necesario describir el proceso de adición en sistema binario y la construcción de los diferentes sumadores para, finalmente, describir la implementación de *HACK*.
## Suma Binaria
Todo en las computadoras se representa mediante el sistema de numeración binario , por lo cual , las computadoras deben encargarse de realizar conversiones decimal-binario y viceversa.Lo anterior es de suma importancia, ya que , realmente las adiciones que realiza *HACK* y demas operaciones lógicas se hacen mediante el uso del sistema binario.<br>
Afortunadamente la suma binaria se realiza bit a bit tal cual como se puede realizar la suma decimal empezando por el par de bit mas a la derecha (LSB) , finalizando con los mas posicionados a la izquierda (MSB) llevando el respectivo accarreo para cada operación.Si la suma bit a bit más significativa genera un acarreo de 1, tenemos lo que se conoce como desbordamiento (*Overflow*). Qué hacer con el desbordamiento es una cuestión de decisión, y para el interes con *HACK* se ignora.<br>
A continuación se muestra un ejemplo de suma binaria:<br>

<img src="https://github.com/user-attachments/assets/a674037d-b3e9-49c5-9975-517dd1e9983d" width="200" height="150" text-align="center"/>
<br>
En las implementaciones de la suma binaria se contaron con tres de estas , que en general una herada de la otra , siendo estas el sumador medio, el sumador completo y el sumador (permite sumar números de n-bits).<br>

## Sumador Medio(*Half Adder*)
El primer paso para la construcción de un sumador completo es la construcción de un sumador medio. El sumador medio es aquel que realiza la suma de dos bits y genera un bit de suma y un bit de acarreo. La tabla de verdad del sumador medio es la siguiente:<br>
| A | B | Suma($\sum$) | Acarreo($C_{out}$) |
|---|---|------|---------|
| 0 | 0 | 0    | 0       |
| 0 | 1 | 1    | 0       |
| 1 | 0 | 1    | 0       |
| 1 | 1 | 0    | 1       |

Donde A y B son los bits de entrada, Suma es el bit de salida y Acarreo es el bit de acarreo. La implementación del sumador medio se realizó en base a las compuertas lógicas *AND*, *OR* y *XOR*.<br>
<img src="https://github.com/user-attachments/assets/0d14e99e-81e0-478f-ac05-4aa0a85f9f13" width="420" height="250" text-align="center"/>
<br>
Por lo cual la salida *Suma* se puede interpretrar como *A XOR B* y la salida *Acarreo* como *A AND B*.Lo anterior tal cual se realizó en la implementación del chip en HDL.<br>

## Sumador Completo(*Full Adder*)
El sumador completo es aquel que realiza la suma de tres bits y genera un bit de suma y un bit de acarreo,el Sumador completo se puede ver como el uso de 2 *Half Adders* : $A+B$ y luego $(A+B)+C_{in}$ , manejando los accarreos de la suma anterior. La tabla de verdad del sumador completo es la siguiente:<br>
| A | B | $C_{in}$ | Suma($\sum$) | Acarreo($C_{out}$) |
|---|---|----------|------|---------|
| 0 | 0 | 0        | 0    | 0       |
| 0 | 0 | 1        | 1    | 0       |
| 0 | 1 | 0        | 1    | 0       |
| 0 | 1 | 1        | 0    | 1       |
| 1 | 0 | 0        | 1    | 0       |
| 1 | 0 | 1        | 0    | 1       |
| 1 | 1 | 0        | 0    | 1       |
| 1 | 1 | 1        | 1    | 1       |
<br>

El Sumador completo , al igual que el medio , se implementó en base a las compuertas lógicas *AND*, *OR* y *XOR* como muestra la siguiente imagen :<br>
<img src="https://github.com/user-attachments/assets/d0bbc8f3-abe8-47c3-a307-33b44718ed3e" width="420" height="250" text-align="center"/>

## Sumador de 16 bits (*16-bit adder*)
El sumador de 16 bits realiza la suma de dos números (bus) de 16 bits cada uno , A y B , realizando la suma bit a bit empezando por el bit menos significativo (LSB) hasta el bit más significativo (MSB) , llevando el acarreo de la suma anterior , por lo cual la implementación es el uso del *Full Adder* anterior visto donde las entradas del mismo son cada bit de izquierda a derecha  y el accarreo ($C_{in}$) es el acarreo de la suma anterior.<br>
<img src="https://github.com/user-attachments/assets/765ccbb7-6280-4418-b226-0afce7477293" width="400" height="240" text-align="center"/>

## Incrementador (*Inc 16*)
<img src="https://github.com/user-attachments/assets/757c3d08-6725-46bb-b4ca-78a3a7dde6c5" width="200" height="200" text-align="center"/>



## ALU (*Arithmetic Logic Unit* : *HACK*)
<img src="https://github.com/user-attachments/assets/5bec398f-b75a-4bf7-9843-d90dd0e5569c" width="350" height="300" text-align="center"/>

La ALU toma varios bits de control como entrada para determinar qué operación realizar. Estos bits de control son:


- $zx$: Si se establece en 1, se establece $x$ en cero.
- $nx$: Si se establece en 1, se realiza una operación de negación en $x$.
- $zy$: Si se establece en 1, se establece y en cero.
- $ny$: Si se establece en 1, se realiza una operación de negación en $y$.
- $f$: Si se establece en 1, se realiza una suma de complemento a 2 $(x + y)$, de lo contrario, se realiza una operación AND $(x \land y)$.
- $no$: Si se establece en 1, se realiza una operación de negación en el resultado.

La ALU tiene tres salidas principales:
- $out$: El resultado de la operación realizada en $x$ e $y$. Es un número de 16 bits.
- $zr$: Si out es igual a cero, $zr$ se establece en 1; de lo contrario, se establece en 0.
- $ng$: Si out es negativo (el bit más significativo es 1), $ng$ se establece en 1; de lo contrario, se establece en 0.
<br>La implementación de la ALU se realiza mediante la manipulación de las entradas $x$ e $y$ y operando en los valores resultantes. Por ejemplo, si $zx$ es 1, $x$ se establece en cero. Si nx es 1, se realiza una operación de negación en $x$. Lo mismo se aplica a las entradas y con $zy$ y $ny$.

Luego, se realiza la operación seleccionada ($f$) en los valores manipulados de $x$ e $y$. Si f es 1, se realiza una suma de complemento a 2 $(x + y)$; de lo contrario, se realiza una operación AND $(x \land y)$

# Proyecto 3: Memorias
En el Proyecto 3 se aborda uno de los pilares fundamentales de la arquitectura de computadoras: la memoria principal, conocida comúnmente como Memoria de Acceso Aleatorio (RAM). Este proyecto desglosa el desafío de cómo almacenar y recuperar datos de manera eficiente y rápida, utilizando registros direccionables de n bits. A lo largo de este proyecto, exploraran la construcción de una unidad RAM completa, comenzando con el diseño de un simple Flip-Flop de Datos (DFF), seguido de chips más complejos como registros individuales y múltiples configuraciones de RAM que varían en capacidad desde 8 registros hasta 16384 registros. El enfoque se centrará en el uso exclusivo de puertas DFF y otros chips fundamentales que se estudiaron en los proyectos anteriores, demostrando la aplicabilidad de la lógica de puertas para solucionar problemas de almacenamiento persistente y direccionamiento efectivo.
Este proyecto tiene como fin, desarrollar y entender el funcionamiento interno de varios chips que componen una unidad RAM, tales como Bit, Register, y diversos tamaños de RAM, desde RAM8 hasta RAM16K, culminando en la creación de un Contador de Programa (PC) de 16 bits. Estos componentes son cruciales para el funcionamiento de cualquier sistema computacional moderno y proporcionan una base sólida para entender conceptos más avanzados en el diseño de sistemas digitales. A través de la implementación y prueba de estos chips utilizando scripts específicos, se reforzarán no solo la comprensión teórica, sino que también adquirirán habilidades prácticas esenciales en la manipulación y diseño de hardware computacional.

## Bit

```
CHIP Bit {
    IN in, load;
    OUT out;

    PARTS:
    // DFF para mantener el estado del bit y proveer salida
    DFF(in=out1, out=dffout, out=out);

    // Mux para decidir el próximo valor del DFF basado en la señal de carga
    Mux(a=dffout, b=in, sel=load, out=out1);
}
```

El Bit es un componente fundamental diseñado para actuar como un registro de un solo bit. Su principal función es almacenar un bit de información, que puede mantenerse o actualizarse según una señal de control llamada load. Si load está activado, el bit almacenado (out) se actualiza con el valor de entrada (in); si no, mantiene su valor anterior.
Para construir este chip, se utilizaron dos partes esenciales: un Flip-Flop de Datos (DFF) y un multiplexor (Mux). El DFF se encarga de mantener el estado actual del bit proporcionando una salida consistente (out). El multiplexor, por otro lado, decide qué valor será retenido en el DFF en el próximo ciclo de reloj. Selecciona entre mantener el valor actual del DFF o actualizarlo con el nuevo valor de entrada, basándose en si la señal de carga está activa. Este diseño permite que el chip Bit funcione de manera efectiva como un registro de memoria básico, fundamental para la construcción de memorias más grandes y complejas.

![chip](https://github.com/user-attachments/assets/10e28815-3a3d-42d9-a270-9ea4de874045)

## Register

```
CHIP Register {
    IN in[16], load;
    OUT out[16];

    PARTS:
    // Crear 16 chips Bit, uno para cada bit del registro
    Bit(in=in[0], load=load, out=out[0]);
    Bit(in=in[1], load=load, out=out[1]);
    Bit(in=in[2], load=load, out=out[2]);
    Bit(in=in[3], load=load, out=out[3]);
    Bit(in=in[4], load=load, out=out[4]);
    Bit(in=in[5], load=load, out=out[5]);
    Bit(in=in[6], load=load, out=out[6]);
    Bit(in=in[7], load=load, out=out[7]);
    Bit(in=in[8], load=load, out=out[8]);
    Bit(in=in[9], load=load, out=out[9]);
    Bit(in=in[10], load=load, out=out[10]);
    Bit(in=in[11], load=load, out=out[11]);
    Bit(in=in[12], load=load, out=out[12]);
    Bit(in=in[13], load=load, out=out[13]);
    Bit(in=in[14], load=load, out=out[14]);
    Bit(in=in[15], load=load, out=out[15]);
}
```

El Register es un registro de 16 bits diseñado para almacenar o actualizar un grupo de bits en base a una señal de control. Este chip es una expansión del concepto básico del chip Bit, replicando su funcionalidad para manejar 16 bits simultáneamente.
En su construcción, el Register utiliza dieciséis instancias del chip Bit, cada uno conectado a uno de los bits de la entrada in[16]. Cada Bit recibe una señal de carga (load) y un bit de entrada (in[i]), y produce un bit de salida (out[i]). Si la señal de carga está activada, cada Bit actualiza su salida al valor correspondiente de la entrada. Si no está activada, cada bit mantiene su valor anterior. Esto permite que el registro completo actualice todos sus 16 bits simultáneamente si se requiere, o mantenga su estado actual, funcionando como una unidad de almacenamiento esencial en la construcción de memorias más complejas y en la operación general de la computadora.

![Register](https://github.com/user-attachments/assets/9afcf153-1d7a-41af-af87-566f62425bde)

## RAM8

```
CHIP RAM8 {
    IN in[16], load, address[3];
    OUT out[16];

    PARTS:
    // Decodificador para convertir address[3] a 8 señales de control
    DMux8Way(in=load, sel=address, a=load0, b=load1, c=load2, d=load3, e=load4, f=load5, g=load6, h=load7);

    // 8 registros
    Register(in=in, load=load0, out=r0);
    Register(in=in, load=load1, out=r1);
    Register(in=in, load=load2, out=r2);
    Register(in=in, load=load3, out=r3);
    Register(in=in, load=load4, out=r4);
    Register(in=in, load=load5, out=r5);
    Register(in=in, load=load6, out=r6);
    Register(in=in, load=load7, out=r7);

    // Multiplexor para seleccionar cuál de los 8 registros mostrar en la salida
    Mux8Way16(a=r0, b=r1, c=r2, d=r3, e=r4, f=r5, g=r6, h=r7, sel=address, out=out);
}
```

La RAM8 es una unidad de memoria compuesta por ocho registros de 16 bits cada uno. Este chip permite almacenar y recuperar datos de cualquier registro seleccionado mediante una dirección específica. La funcionalidad del chip se centra en dos operaciones principales: cargar un valor en un registro seleccionado y emitir el valor de un registro según la dirección especificada.
Para lograr esto, el chip utiliza un decodificador DMux8Way que toma una señal de carga y una dirección de tres bits, dividiendo la señal de carga entre ocho líneas de control (load0 a load7), cada una correspondiente a uno de los registros. Dependiendo de la dirección proporcionada, solo una línea de control se activará, permitiendo cargar datos únicamente en el registro deseado. Además, se utilizan ocho chips Register para almacenar los datos. Cada registro recibe datos de entrada y la señal de carga correspondiente, y mantiene o actualiza su contenido basándose en el estado de esta señal. Finalmente, un multiplexor Mux8Way16 selecciona la salida de uno de estos ocho registros para emitir, basándose también en la dirección suministrada. Esta estructura hace que el RAM8 sea un componente crucial para gestionar múltiples bloques de datos en sistemas computacionales, permitiendo un acceso rápido y eficiente a distintos conjuntos de información.

![ram8](https://github.com/user-attachments/assets/92318c07-60ea-42e3-804c-27362c6c411a)

## RAM64

```
CHIP RAM64 {
    IN in[16], load, address[6];
    OUT out[16];

    PARTS:
    // Dividir la dirección en partes para seleccionar el RAM8 y el registro dentro de ese RAM8
    DMux8Way(in=load, sel=address[3..5], a=loadA, b=loadB, c=loadC, d=loadD, e=loadE, f=loadF, g=loadG, h=loadH);

    // Ocho chips RAM8
    RAM8(in=in, load=loadA, address=address[0..2], out=ra);
    RAM8(in=in, load=loadB, address=address[0..2], out=rb);
    RAM8(in=in, load=loadC, address=address[0..2], out=rc);
    RAM8(in=in, load=loadD, address=address[0..2], out=rd);
    RAM8(in=in, load=loadE, address=address[0..2], out=re);
    RAM8(in=in, load=loadF, address=address[0..2], out=rf);
    RAM8(in=in, load=loadG, address=address[0..2], out=rg);
    RAM8(in=in, load=loadH, address=address[0..2], out=rh);

    // Mux para seleccionar la salida correcta
    Mux8Way16(a=ra, b=rb, c=rc, d=rd, e=re, f=rf, g=rg, h=rh, sel=address[3..5], out=out);
}
```

La RAM64 es una extensión del chip RAM8, diseñado para gestionar un conjunto más amplio de datos a través de sesenta y cuatro registros de 16 bits. Esta unidad de memoria emplea una estructura más compleja para manejar el aumento en el número de registros, permitiendo una carga y recuperación eficiente de datos en cualquiera de estos registros mediante una dirección específica.
La implementación de la RAM64 comienza con la subdivisión de la dirección de 6 bits en dos partes: los tres bits superiores se utilizan para seleccionar uno de los ocho chips RAM8 mediante un decodificador DMux8Way, mientras que los tres bits inferiores determinan el registro específico dentro del RAM8 seleccionado. Cada RAM8 recibe la misma entrada de datos y una señal de carga controlada por el DMux8Way, que activa la carga en un único RAM8 basado en la parte superior de la dirección. Esto asegura que sólo el RAM8 seleccionado puede modificar sus registros.
Finalmente, un multiplexor Mux8Way16 se encarga de seleccionar y emitir los datos del registro adecuado de entre los ocho RAM8 basándose en los bits de dirección superiores. Este diseño permite al RAM64 operar como una memoria cohesiva de 64 registros, manteniendo la eficiencia y la especificidad en el acceso y la modificación de datos, lo cual es esencial para el manejo de grandes volúmenes de información en sistemas computacionales avanzados.

![Ram64](https://github.com/user-attachments/assets/ef6288e9-c0dc-41ef-b9b9-1123085f22da)

## RAM512

```
CHIP RAM512 {
    IN in[16], load, address[9];
    OUT out[16];

    PARTS:
    // Dividir la dirección en partes para seleccionar el RAM64 y el registro dentro de ese RAM64
    DMux8Way(in=load, sel=address[6..8], a=loadA, b=loadB, c=loadC, d=loadD, e=loadE, f=loadF, g=loadG, h=loadH);

    // Ocho chips RAM64
    RAM64(in=in, load=loadA, address=address[0..5], out=ra);
    RAM64(in=in, load=loadB, address=address[0..5], out=rb);
    RAM64(in=in, load=loadC, address=address[0..5], out=rc);
    RAM64(in=in, load=loadD, address=address[0..5], out=rd);
    RAM64(in=in, load=loadE, address=address[0..5], out=re);
    RAM64(in=in, load=loadF, address=address[0..5], out=rf);
    RAM64(in=in, load=loadG, address=address[0..5], out=rg);
    RAM64(in=in, load=loadH, address=address[0..5], out=rh);

    // Mux para seleccionar la salida correcta
    Mux8Way16(a=ra, b=rb, c=rc, d=rd, e=re, f=rf, g=rg, h=rh, sel=address[6..8], out=out);
}
```

La RAM512 es una memoria diseñada para almacenar datos en 512 registros de 16 bits cada uno. Al igual que los chips de menor capacidad, su funcionamiento se basa en dividir la dirección en partes para seleccionar el registro correcto. En este caso, se utiliza un esquema jerárquico que permite gestionar eficientemente una memoria más grande.
Para lograrlo, la dirección de 9 bits se divide en dos secciones. Los tres bits superiores (address[6..8]) se utilizan para seleccionar uno de las ocho chips RAM64, mediante un decodificador DMux8Way, que envía la señal de carga a una de las RAM64 correspondientes. Los seis bits restantes de la dirección (address[0..5]) se utilizan para seleccionar el registro específico dentro del RAM64 activado.
Cada uno de los ocho chips RAM64 maneja 64 registros de 16 bits, y el multiplexor Mux8Way16 se encarga de seleccionar la salida correcta entre los ocho RAM64 según los bits superiores de la dirección. Este diseño permite que el chip RAM512 almacene una gran cantidad de datos de manera eficiente y acceda rápidamente a cualquier registro, expandiendo la capacidad de memoria en un sistema computacional.

<Imagen>

## RAM4K

```
CHIP RAM4K {
    IN in[16], load, address[12];
    OUT out[16];

    PARTS:
    // Dividir la dirección en partes para seleccionar el RAM512 y el registro dentro de ese RAM512
    DMux8Way(in=load, sel=address[9..11], a=loadA, b=loadB, c=loadC, d=loadD, e=loadE, f=loadF, g=loadG, h=loadH);

    // Ocho chips RAM512
    RAM512(in=in, load=loadA, address=address[0..8], out=ra);
    RAM512(in=in, load=loadB, address=address[0..8], out=rb);
    RAM512(in=in, load=loadC, address=address[0..8], out=rc);
    RAM512(in=in, load=loadD, address=address[0..8], out=rd);
    RAM512(in=in, load=loadE, address=address[0..8], out=re);
    RAM512(in=in, load=loadF, address=address[0..8], out=rf);
    RAM512(in=in, load=loadG, address=address[0..8], out=rg);
    RAM512(in=in, load=loadH, address=address[0..8], out=rh);

    // Mux para seleccionar la salida correcta
    Mux8Way16(a=ra, b=rb, c=rc, d=rd, e=re, f=rf, g=rg, h=rh, sel=address[9..11], out=out);
}
```

La RAM4K es una unidad de memoria que permite almacenar datos en 4096 registros de 16 bits cada uno. Este diseño se basa en una estructura jerárquica similar a los chips anteriores, pero a mayor escala, dividiendo la memoria en bloques manejables para facilitar el acceso y la actualización de los datos.
Para lograrlo, se utiliza una dirección de 12 bits, que se divide en dos partes. Los tres bits superiores de la dirección (address[9..11]) son utilizados por un decodificador DMux8Way para seleccionar uno de los ocho chips RAM512, enviando la señal de carga al chip correspondiente. Los nueve bits restantes (address[0..8]) se pasan al chip RAM512 seleccionado, que internamente gestiona sus 512 registros.
Cada chip RAM512 contiene 512 registros de 16 bits, y el multiplexor Mux8Way16 selecciona la salida correcta de entre los ocho RAM512 basándose en los tres bits superiores de la dirección. Este diseño permite manejar grandes volúmenes de datos de manera eficiente y estructurada, asegurando un acceso rápido y organizado dentro de los 4096 registros totales.

<Imagen>

## RAM16K

```
CHIP RAM16K {
    IN in[16], load, address[14];
    OUT out[16];

    PARTS:
    /* Los tres bits más significativos seleccionan cuál de los ocho chips RAM4K
     * cargar, mientras que los once bits menos significativos seleccionan
     * el registro dentro de ese RAM4K */
    DMux8Way(in=load, sel=address[11..13], a=load0, b=load1, c=load2, d=load3, e=load4, f=load5, g=load6, h=load7);

    // Ocho chips RAM4K, cada uno con su propio `load` y dirección
    RAM4K(in=in, load=load0, address=address[0..11], out=ram0);
    RAM4K(in=in, load=load1, address=address[0..11], out=ram1);
    RAM4K(in=in, load=load2, address=address[0..11], out=ram2);
    RAM4K(in=in, load=load3, address=address[0..11], out=ram3);
    RAM4K(in=in, load=load4, address=address[0..11], out=ram4);
    RAM4K(in=in, load=load5, address=address[0..11], out=ram5);
    RAM4K(in=in, load=load6, address=address[0..11], out=ram6);
    RAM4K(in=in, load=load7, address=address[0..11], out=ram7);

    // Mux para seleccionar la salida del RAM4K correcto
    Mux8Way16(a=ram0, b=ram1, c=ram2, d=ram3, e=ram4, f=ram5, g=ram6, h=ram7, sel=address[11..13], out=out);
}
```

La RAM16K es una memoria que permite almacenar datos en 16,384 registros de 16 bits, empleando una estructura jerárquica que organiza la memoria en bloques más pequeños y manejables. Este diseño expande la capacidad de almacenamiento mediante la combinación de ocho chips RAM4K, cada uno encargado de 4096 registros.
El funcionamiento de este chip se basa en dividir la dirección de 14 bits en dos partes. Los tres bits más significativos (address[11..13]) se utilizan para seleccionar cuál de los ocho chips RAM4K activará su señal de carga mediante un decodificador DMux8Way. Los once bits restantes de la dirección (address[0..11]) se envían al RAM4K seleccionado, donde se accede al registro específico dentro de ese bloque de 4096 registros.
Una vez que el chip RAM4K apropiado ha sido seleccionado y cargado, un multiplexor Mux8Way16 se encarga de seleccionar la salida correcta, emitiendo los datos almacenados en el registro especificado. Este diseño permite que el chip RAM16K gestione grandes cantidades de datos de manera eficiente, manteniendo la estructura modular que facilita su implementación en sistemas computacionales avanzados.

![ram16k](https://github.com/user-attachments/assets/635f5ff7-00c4-4226-b318-b8759fdcb97d)

## PC

```
CHIP PC {
    IN in[16], load, inc, reset;
    OUT out[16];

    PARTS:
    /* Incrementar el registro: provee la funcionalidad de "contar" (incrementar). */
    Inc16(in=reg, out=increg);

    /* Ahora colocamos el contador en el modo de operación correcto. Los tres bits de control
    nos indican si la salida debe ser incrementada, cargada con una nueva base de conteo
    o reiniciada a cero, según se especifica en la API. */
    Mux16(a=reg, b=increg, sel=inc, out=o1);   // Selección entre el valor actual y el valor incrementado
    Mux16(a=o1, b=in, sel=load, out=o2);       // Selección entre el valor incrementado o el valor de entrada
    Mux16(a=o2, b=false, sel=reset, out=o3);   // Selección entre el valor de entrada o el valor "0" (reset)
    Register(in=o3, load=true, out=out, out=reg);  // Registro que guarda el valor final
}
```

El chip PC (Contador de Programa) es responsable de manejar el conteo secuencial de instrucciones en una computadora. Su principal función es almacenar y actualizar el valor de una dirección de memoria, que puede ser incrementada, cargada con un valor específico o reiniciada a cero, según las señales de control proporcionadas (inc, load y reset).

La construcción del PC comienza con la utilización de un chip Inc16, que toma el valor actual del registro (reg) y lo incrementa en uno, permitiendo la funcionalidad de "contar" en el chip. A continuación, una serie de multiplexores (Mux16) se encargan de seleccionar la operación correcta según las señales de control: si se debe incrementar el valor del registro, cargar un nuevo valor (in), o reiniciar el registro a cero. Finalmente, un registro (Register) almacena el valor resultante y lo mantiene como la salida del chip (out). Esta estructura permite al PC operar de manera flexible y eficiente, proporcionando la capacidad de controlar el flujo de ejecución en un sistema computacional.

![pc](https://github.com/user-attachments/assets/7c31349b-df63-4125-820b-ac5cbde538f8)


# Referencias
<ul>
<li>Nisan, N., & Schocken, S. (2021). The elements of computing systems: building a modern computer from first principles. MIT press
<li>Floyd, T. (2015). Digital Fundamentals/Floyd T.
<ul>
