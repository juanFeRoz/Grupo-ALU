# Respuestas - Preguntas Adicionales (Práctica 2)

### 1. Objetivo de los Proyectos de Nand2Tetris
El objetivo de los proyectos en NAND2TETRIS es guiar al estudiante en la construcción de una computadora completa desde sus componentes más básicos hasta un sistema funcional capaz de ejecutar programas complejos. A través de doce proyectos, el enfoque es construir de manera gradual módulos de hardware y software, como unidades de memoria, procesadores, un lenguaje ensamblador, un compilador, y finalmente un sistema operativo simple. Estos proyectos enseñan desde la creación de compuertas lógicas hasta el diseño de un compilador. El objetivo final es tener una comprensión completa del funcionamiento de los sistemas de cómputo desde una perspectiva tanto de hardware como de software​.

Para desarrollar estos proyectos, se deben seguir una serie de pasos específicos. Por ejemplo, el primer proyecto implica construir compuertas lógicas usando HDL (Hardware Description Language), mientras que otros proyectos posteriores se enfocan en el diseño y construcción de la unidad lógica-aritmética (ALU), memoria RAM, CPU, y finalmente la creación de un compilador y un sistema operativo. Cada proyecto está diseñado para ser modular, lo que significa que los bloques construidos en los primeros proyectos se utilizan en los subsiguientes​.

### 2. Lógica Aritmética vs Lógica Secuencial
La lógica aritmética se refiere a operaciones combinacionales donde los resultados dependen únicamente de las entradas actuales. Un ejemplo clásico es una unidad lógica-aritmética (ALU), la cual realiza operaciones como suma, resta, y operaciones lógicas (AND, OR) sin tener en cuenta un estado previo. Es determinística, lo que significa que para una entrada dada, siempre produce la misma salida​.

En cambio, la lógica secuencial implica circuitos que, además de sus entradas actuales, también dependen del estado previo. Estos circuitos utilizan dispositivos como flip-flops para almacenar el estado, lo que les permite recordar información entre ciclos de reloj. Un ejemplo típico de lógica secuencial es un contador, que actualiza su valor con cada pulso de reloj basándose en el estado anterior. La característica clave de la lógica secuencial es la dependencia del tiempo y el uso de un "estado", lo que la diferencia de la lógica puramente combinacional.

### Bonus. Tipos de Unidades Aritmético Lógicas
Los tipos de ALU que existen incluyen las de coma fija y las de coma flotante. Una ALU de coma fija utiliza un número fijo de dígitos para representar la parte entera y la parte fraccionaria de un número, lo que implica que la posición de la coma es constante. Estas ALUs son más rápidas pero menos flexibles para manejar un rango amplio de valores numéricos. Por otro lado, una ALU de coma flotante permite que la posición de la coma varíe, lo que le otorga la capacidad de manejar números extremadamente grandes o pequeños con mayor precisión, siendo ideal para cálculos científicos complejos.

### Referencias

- [Unidad aritmética lógica (ALU)](https://es.slideshare.net/slideshow/unidad-aritmtica-lgica-alu-250586922/250586922)
- Nisan, N., & Schocken, S. (2021). The elements of computing systems: building a modern computer from first principles. MIT press
