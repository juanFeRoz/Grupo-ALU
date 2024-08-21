# Práctica : Lógica Booleana
Los dispositivos digitales que empleamos hoy en día , como nuestros télefonos inteligentes,computadoras y demas dispositivos, estan conformados por un conjunto de chips que estan diseñados para procesar y almacenar la información necesaria para dichos dispositivos.
Por lo cual se hace necesario comprender el funcionamiento básico de los componentes (chips) , tambien denominados compuertas , que parten como el componente básico para nuestro estudio de arquitectura de computadoras.
Una compuerta es un dispositivo físico que implementa una función lógica , como And , Or , XOr y las diferentes operaciones que se pueden realizar entre ellas combinandolas entre si.

## Implementacion de los chips

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
### Mux
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

### DMux

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
