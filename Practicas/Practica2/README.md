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

# Referencias
<ul>
<li>Nisan, N., & Schocken, S. (2021). The elements of computing systems: building a modern computer from first principles. MIT press
<li>Floyd, T. (2015). Digital Fundamentals/Floyd T.
<ul>
