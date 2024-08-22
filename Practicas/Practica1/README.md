# Práctica : Lógica Booleana
<p style='text-align:justify;'>
Los dispositivos digitales que empleamos hoy en día , como nuestros télefonos inteligentes,computadoras y demas dispositivos, estan conformados por un conjunto de chips que estan diseñados para procesar y almacenar la información necesaria para dichos dispositivos.
Por lo cual se hace necesario comprender el funcionamiento básico de los componentes (chips) , tambien denominados compuertas , que parten como el componente básico para nuestro estudio de arquitectura de computadoras.<br>
Una compuerta es un dispositivo físico que implementa una función lógica , como And , Or , XOr y las diferentes operaciones que se pueden realizar entre ellas combinandolas entre si.El proyecto 1 nos plantea como a partir del proceso de abstracción de las compuertas lógicas, estas se pueden implementar eficientemente empleando compuertas ya implementadas, siendo mas especificos para dicho proyecto , a partir de la compuerta universal NAnd se construiran el conjunto elemental de compuertas lógicas And , Or , XOr , Mux , las versiones bit a bit y las multidireccionales.La implementación se realizó con el uso del lengujae HDL implementado en el proyecto NAND2Tetris.<p><br>
En este repositorio se podran encontrar alojados todas las implementaciones de las compuertas en sus respectivos archivos HDL, ademas , se encontraran las respuestas a las preguntas adicionales planteadas para esta práctica.

## Implementación de los chips en HDL

### NOT

![images](https://github.com/user-attachments/assets/50e68a81-1c3b-4afa-a19a-0cc1b085511a)

En la tabla de verdad del chip NAND se puede observar que cuando los inputs son iguales la compuerta los invierte, lo cual es el comportamiento deseado para el chip NOT

![Untitled](https://github.com/user-attachments/assets/0877e95d-0aca-40c0-b5f2-2f4357aee46b)

En la implementacion se paso el mismo input a las dos entradas del NAND para emular el comportamiento del NOT

```
CHIP Not {
    IN in;
    OUT out;

    PARTS:
    Nand(a=in , b= in, out=out);
}
```

### AND

![1218022_1511917_ans_f5abd499d0c44e4e988017391724e31e](https://github.com/user-attachments/assets/e22634d8-8d35-4f60-ab88-76d4ba9a9559)

Teniendo en cuenta que el NAND es un AND con la salida invertida por un NOT se decidio utilizar el principio de la doble negación para implementar el chip. Simplemente invirtiendo la salida del chip NAND se consigue emular el comportamiento del AND

```
CHIP And {
    IN a, b;
    OUT out;
    
    PARTS:
    Nand(a=a , b=b , out=outnan);
    Not(in=outnan , out=out );
}
```

### OR

![657636_623645_ans_b5043da31fb448249144c1398f9d83eb](https://github.com/user-attachments/assets/13f537e1-d316-46d5-ad31-2c7e71169e54)

Usando la ley de D'Morgan se deduce que el NAND es un OR con sus dos entradas invertidas, por lo tanto si se invierten de nuevo las dos entradas del NAND terminamos con una compuerta OR gracias a la ley de doble negacion.

```
CHIP Or {
    IN a, b;
    OUT out;

    PARTS:
    Not(in=a , out=nota );
    Not(in=b, out=notb );
    And(a=nota , b=notb , out=notand );
    Not(in=notand , out=out );
}
```

### XOR

El circuito que implementa la compuerta XOR puede entenderse mediante el uso de compuertas lógicas básicas como Not, And, y Or.

![image](https://github.com/user-attachments/assets/3c20693f-5a63-43d0-a4db-1c50ecce26f4)

La operación XOR (o "Exclusive OR") se define de la siguiente manera: la salida es 1 si una y solo una de las dos entradas es 1. Esto significa que si ambas entradas son iguales, la salida será 0.

```
CHIP Xor {
    IN a, b;
    OUT out;

    PARTS:
    Not(in=a , out=na );
    Not(in=b , out=nb );
    And(a=na , b=b , out=and1 );
    And(a=a , b=nb , out=and2 );
    Or(a=and1 , b=and2 , out=out );
}
```
La compuerta XOR se puede ver como una combinación de condiciones donde se detecta cuando las entradas son diferentes. Al combinar estas condiciones con una OR, obtenemos la operación deseada. El uso de la negación en las entradas y en las condiciones intermedias es lo que permite implementar la función XOR de manera eficiente.

### MUX

![image](https://github.com/user-attachments/assets/8738b205-2edf-42bd-a7a9-b8a20d4b5ff3)

Un multiplexor que recibe dos señales como input y selecciona una de las dos como output. Se implemento a partir de las expresiones logicas derivadas de su tabla de verdad simplificada. Si *sel* es 0, el output es igual a la señal *a* y cuando *sel* es 1, el output sera igual a *b*

```
CHIP Mux {
    IN a, b, sel;
    OUT out;

    PARTS:
    Not(in=sel, out=notsel);
    And(a=notsel , b=a , out=sel0 );
    And(a=sel , b=b , out=sel1 );
    Or(a=sel0 , b=sel1 , out=out );
}
```

### DMUX

![image](https://github.com/user-attachments/assets/f31cbfd8-7ad1-40f3-953a-5ab615dca1d2)

Actua como el inverso de un Mux, pues distribuye una entrada en una de dos posibles salidas. Para implementarlo basta con observar la tabla de verdad y ver que la salida *a* solo sera 1 si y solo si *in* es 1 y *sel* es 0, y la salida *b* es 1 si y solo si *in* es 1 y *sel* tambien es 1  

```
CHIP DMux {
    IN in, sel;
    OUT a, b;

    PARTS:
    And(a=in , b=sel , out=b );
    Not(in=sel , out=notsel );
    And(a=in , b=notsel , out=a );
}
```

### NOT16

![not16](https://github.com/user-attachments/assets/efa6d35b-0dd7-4ffb-b5fd-f672c5823f68)

El circuito Not16 implementa una operación de negación bit a bit sobre un bus de 16 bits. Esto significa que cada bit de la entrada se invierte individualmente para producir la salida correspondiente.

```
CHIP Not16 {
    IN in[16];
    OUT out[16];

    PARTS:
    Not(in=in[0] , out=out[0] );
    Not(in=in[1] , out=out[1] );
    Not(in=in[2] , out=out[2] );
    Not(in=in[3] , out=out[3] );
    Not(in=in[4] , out=out[4] );
    Not(in=in[5] , out=out[5] );
    Not(in=in[6] , out=out[6] );
    Not(in=in[7] , out=out[7] );
    Not(in=in[8] , out=out[8] );
    Not(in=in[9] , out=out[9] );
    Not(in=in[10] , out=out[10] );
    Not(in=in[11] , out=out[11] );
    Not(in=in[12] , out=out[12] );
    Not(in=in[13] , out=out[13] );
    Not(in=in[14] , out=out[14] );
    Not(in=in[15] , out=out[15] );
}
```

### AND16

![And16](https://github.com/user-attachments/assets/ab960ad2-0915-441d-8bd4-299078f44baf)

Una compuerta And16 aplica la operación Booleana And a cada respectivo par de entradas. Para su funcionamiento se utiliza un par de arreglos de 16 elementos para un total de 32 entradas y, un arreglo de 16 elementos para la salida.

```
CHIP And16 {
    IN a[16], b[16];
    OUT out[16];

    PARTS:
    And(a=a[0] , b=b[0] , out=out[0] );
    And(a=a[1] , b=b[1] , out=out[1] );
    And(a=a[2] , b=b[2] , out=out[2] );
    And(a=a[3] , b=b[3] , out=out[3] );
    And(a=a[4] , b=b[4] , out=out[4] );
    And(a=a[5] , b=b[5] , out=out[5] );
    And(a=a[6] , b=b[6] , out=out[6] );
    And(a=a[7] , b=b[7] , out=out[7] );
    And(a=a[8] , b=b[8] , out=out[8] );
    And(a=a[9] , b=b[9] , out=out[9] );
    And(a=a[10] , b=b[10] , out=out[10] );
    And(a=a[11] , b=b[11] , out=out[11] );
    And(a=a[12] , b=b[12] , out=out[12] );
    And(a=a[13] , b=b[13] , out=out[13] );
    And(a=a[14] , b=b[14] , out=out[14] );
    And(a=a[15] , b=b[15] , out=out[15] );
}
```

### OR16

![Or16](https://github.com/user-attachments/assets/9c5f7c4d-a17b-44ab-85fa-ba2301a4d004)

Una compuerta Or16 aplica la operación Booleana Or a cada respectivo par de entradas. Para su funcionamiento se utiliza un par de arreglos de 16 elementos para un total de 32 entradas y, un arreglo de 16 elementos para la salida.

```
CHIP Or16 {
    IN a[16], b[16];
    OUT out[16];

    PARTS:
    Or(a=a[0] , b=b[0] , out=out[0] );
    Or(a=a[1] , b=b[1] , out=out[1] );
    Or(a=a[2] , b=b[2] , out=out[2] );
    Or(a=a[3] , b=b[3] , out=out[3] );
    Or(a=a[4] , b=b[4] , out=out[4] );
    Or(a=a[5] , b=b[5] , out=out[5] );
    Or(a=a[6] , b=b[6] , out=out[6] );
    Or(a=a[7] , b=b[7] , out=out[7] );
    Or(a=a[8] , b=b[8] , out=out[8] );
    Or(a=a[9] , b=b[9] , out=out[9] );
    Or(a=a[10] , b=b[10] , out=out[10] );
    Or(a=a[11] , b=b[11] , out=out[11] );
    Or(a=a[12] , b=b[12] , out=out[12] );
    Or(a=a[13] , b=b[13] , out=out[13] );
    Or(a=a[14] , b=b[14] , out=out[14] );
    Or(a=a[15] , b=b[15] , out=out[15] );
}
```

### MUX4WAY16

Esta compuerta es un multiplexor que selecciona una de las cuatro entradas para cada cuarteto de bits , realizando el proceso para cada uno de los 16 cuartetos de bits para los 4 buses de entrada a,b,c y d.La selección se realiza mediante los 2 bits de selección bajo la siguiendo la siguiente lógica : <br>

![imagen](https://github.com/user-attachments/assets/c4fabdc8-0cbb-4da1-8034-cb332dfea8fd)

```
CHIP Mux4Way16 {
    IN a[16], b[16], c[16], d[16], sel[2];
    OUT out[16]; 
    PARTS:
    Mux16(a=a,b=b,sel=sel[0],out=o1);
    Mux16(a=c,b=d,sel=sel[0],out=o2);
    Mux16(a=o1,b=o2,sel=sel[1],out=out);
}
```

### MUX8WAY16

![mux8way16](https://github.com/user-attachments/assets/6bb6f6af-df5e-4c4b-8c24-29ac7f3f0854)

funciona como un multiplexor de 8 entradas de 16 bits cada una. Usa una selección de 3 bits (sel[3]) para determinar cuál de las 8 entradas (a, b, c, d, e, f, g, h) se enviará a la salida de 16 bits (out[16]).

```
CHIP Mux8Way16 {
    IN a[16], b[16], c[16], d[16],
       e[16], f[16], g[16], h[16],
       sel[3];
    OUT out[16];
    PARTS:
    Mux16(a=a,b=b,sel=sel[0],out=o1);
    Mux16(a=c,b=d,sel=sel[0],out=o2);
    Mux16(a=o1,b=o2,sel=sel[1],out=o3);
    Mux16(a=e,b=f,sel=sel[0],out=o4);
    Mux16(a=g,b=h,sel=sel[0],out=o5);
    Mux16(a=o4,b=o5,sel=sel[1],out=o6);
    Mux16(a=o3,b=o6,sel=sel[2],out=out);
}
```
### DMUX4WAY

Este componente lógico es un demultiplexor (DMux) de 4 vías que recibe una entrada (in) junto con dos señales de selección (sel[0] y sel[1]), y redirige la entrada a una de las cuatro salidas posibles (a, b, c o d) dependiendo del valor de las señales de selección. <br>

![imagen](https://github.com/user-attachments/assets/2a57b45c-f932-4048-ae76-61e7be4e9827)

```
CHIP DMux4Way {
    IN in, sel[2];
    OUT a, b, c, d;
    PARTS:
    DMux(in=in,sel=sel[1],a=o1,b=o2);
    DMux(in=o1,sel=sel[0],a=a,b=b);
    DMux(in=o2,sel=sel[0],a=c,b=d);
}
```

### DMUX8WAY

Este dispositivo convierte una entrada única en ocho salidas posibles (a, b, c, d, e, f, g o h) mediante tres señales de selección. Este proceso se realiza en dos etapas: primero, un DMux divide la entrada en dos rutas, y luego, dos DMux4Way toman cada una de esas rutas y las dividen en cuatro salidas finales según los valores de las señales de selección. <br>
![image](https://github.com/user-attachments/assets/e3c6b200-ad7c-4c2d-94ab-411e31d7e25d)

```
CHIP DMux8Way {
    IN in, sel[3];
    OUT a, b, c, d, e, f, g, h;
    PARTS:
    DMux(in=in,sel=sel[2],a=o1,b=o2);
    DMux4Way(in=o1,sel=sel[0..1],a=a,b=b,c=c,d=d);
    DMux4Way(in=o2,sel=sel[0..1],a=e,b=f,c=g,d=h);
}
```



## <b>REFERENCIAS<b>
<ul>
<li>Nisan, N., & Schocken, S. (2021). The elements of computing systems: building a modern computer from first principles. MIT press
<ul>
