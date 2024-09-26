# Respuestas - Preguntas Adicionales (Práctica 3)

### 1. Importancia del Lenguaje de Máquina en la Definición de la Arquitectura Computacional
El lenguaje de máquina es crucial en la definición de la arquitectura computacional porque actúa como el mediador entre el software y el hardware. Este lenguaje está compuesto por instrucciones binarias que la CPU puede entender y ejecutar directamente, sin necesidad de traducción adicional. Cada tipo de procesador tiene su propio conjunto único de instrucciones de lenguaje de máquina, también conocidas como conjunto de instrucciones. La elección y el diseño de este conjunto de instrucciones influyen profundamente en la arquitectura del hardware, incluyendo cómo se diseñan la CPU, la memoria y los subsistemas de entrada/salida. Por ejemplo, en el Hack Computer, el conjunto de instrucciones de máquina define operaciones específicas que la ALU debe realizar y cómo se manejan los registros dentro del CPU, aspectos que son fundamentales para el diseño y funcionamiento del hardware.

### 2. Diferencia entre Arquitectura Computacional, Arquitectura de Software y Arquitectura del Sistema
La arquitectura computacional se refiere al diseño estructural de los componentes de hardware de una computadora y la manera en que interactúan estos componentes entre sí, incluyendo procesadores, memoria y sistemas de entrada/salida. Está muy influenciada por el lenguaje de máquina y tiene un enfoque fuerte en la eficiencia y optimización del hardware.

La arquitectura de software, por otro lado, implica el diseño y la organización de los sistemas de software. Esto incluye la definición de subcomponentes de software, sus interfaces y las interacciones entre ellos para cumplir con los requisitos del negocio o del usuario final. La arquitectura de software trata más sobre patrones y principios de diseño que se aplican para crear sistemas de software escalables, mantenibles y eficientes.

La arquitectura del sistema es un concepto más amplio que abarca tanto el hardware como el software. Incluye la configuración completa del sistema informático y la integración de sus componentes físicos y lógicos para trabajar juntos de manera efectiva. Esto puede incluir la infraestructura de red, los servidores, los dispositivos de almacenamiento, así como el software que se ejecuta en estos dispositivos, enfocándose en cómo el sistema completo se comporta y se gestiona para cumplir con los requisitos del proyecto o de la empresa.

### Bonus: Relación entre Arquitectura Computacional, del Sistema y de Software
En la práctica profesional de la informática, aunque las arquitecturas computacional y del sistema toman en cuenta el hardware principalmente, no pueden ser completamente aisladas de la arquitectura de software. Esto es porque el diseño del software tiene un impacto significativo en cómo se debe configurar y optimizar el hardware. Por ejemplo, un sistema que requiere una gran cantidad de procesamiento de datos en tiempo real, como un sistema de trading de alta frecuencia, no solo necesita un hardware poderoso y bien configurado sino también un software altamente eficiente que pueda aprovechar al máximo el hardware subyacente.

Además, las decisiones de arquitectura de software pueden limitar o ampliar las opciones de arquitectura de hardware y de sistema. Por ejemplo, la elección de ciertas tecnologías o frameworks puede influir en la configuración del sistema operativo, la selección del hardware o incluso la topología de red necesaria. Así, un enfoque integrado que considere tanto la arquitectura de software como la de hardware y del sistema es esencial para el éxito del diseño y la implementación de sistemas informáticos complejos.

### Referencias

- Nisan, N., & Schocken, S. (2021). The elements of computing systems: building a modern computer from first principles. MIT press
