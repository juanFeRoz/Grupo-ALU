# Respuestas - Preguntas Adicionales (Práctica 4)

### 1.  Limitante del Ensamblador

La principal limitante observada en el ensamblador es su incapacidad para traducir adecuadamente programas que incluyen lógica compleja y elementos interactivos, como `Pong.asm` y `PongL.asm`. Estos programas requieren un manejo más sofisticado de símbolos y condiciones dinámicas, algo que el ensamblador básico puede no poder realizar eficientemente. La implementación del ensamblador está diseñada para traducir programas escritos en un lenguaje simbólico, lo que significa que debe gestionar la conversión de instrucciones a su representación binaria. Sin embargo, los desafíos surgen al tratar de traducir instrucciones que dependen de la interacción del usuario o de la lógica del juego en tiempo real. Esto se convierte en una limitante crítica, ya que, aunque el ensamblador ha demostrado ser efectivo para la mayoría de los programas de prueba, su incapacidad para manejar adecuadamente estos casos más complejos revela la necesidad de mejoras significativas.

Además, el hecho de implementar el ensamblador en un lenguaje de alto nivel lo hace poco práctico y muy poco escalable, ya que los lenguajes de alto nivel no permiten el acceso directo a operaciones del hardware. Como se menciona en el capítulo 6 del libro "The Elements of Computing Systems", el ensamblador debe ser capaz de interpretar no solo los comandos básicos, sino también las referencias a memoria y a los símbolos que se utilizan en contextos más avanzados, lo que no se logró en los programas de Pong.

### Bonus. Importancia del Ensamblador

El ensamblador es fundamental en el contexto del desarrollo de software y la comprensión de la informática a nivel bajo. Su papel principal es servir como un puente entre el código de alto nivel y el hardware de la computadora, traduciendo instrucciones comprensibles para los programadores en un formato que la máquina puede ejecutar. Esta capacidad de traducción no solo permite que los programas se ejecuten, sino que también ayuda a los desarrolladores a aprender sobre la arquitectura del sistema y los mecanismos subyacentes que permiten la ejecución de código.

A medida que se construye el ensamblador, se sientan las bases para futuros desarrollos, incluyendo la creación de un compilador para lenguajes de alto nivel como Java, el objetivo final del proyecto Nand to Tetris. A pesar de su éxito en la mayoría de las pruebas, la incapacidad para manejar adecuadamente los casos más complejos, como los presentados por Pong, subraya la necesidad de seguir desarrollando y mejorando el ensamblador. Este proceso de perfeccionamiento no solo es crucial para los programas que se están construyendo, sino que también es vital para una educación informática sólida, que enfatiza la comprensión del funcionamiento interno de las máquinas y la programación a nivel bajo. 

La evolución del ensamblador es, por lo tanto, una parte esencial del viaje hacia el dominio completo de la programación y la informática.

### Referencias

- Nisan, N., & Schocken, S. (2021). The elements of computing systems: building a modern computer from first principles. MIT press
