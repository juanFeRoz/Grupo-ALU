// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.


//initialize the control variable in the top-left of the screen
@PIXEL
M=0
//loop for control the keyboard events
(LOOP)
    @KBD
    D=M
    //If the input of the keyboard if 0 , meaning that don't press any keys on the keyboard
    @WHITE
    D;JEQ
    @BLACK
    D;JGT
(WHITE)
    @PIXEL
    D=M
    @LOOP
    D;JEQ
    //Get the current pixel
    @PIXEL
    D=M
    @SCREEN
    A=D+A
    //Change the pixel to white
    M=0
    //Move to the previous pixel
    @PIXEL
    M=M-1
    //Go to the Loop fot the next keyboard input
    @LOOP
    0;JMP
(BLACK)
    @PIXEL
    D=M
    //Maximum number of words that can be written on the screen
    //256 rows × 32 words per row = 8192 words
    @8192
    D=D-A
    //Go to the keyboard input if this is an overflow
    @LOOP
    D;JGE
    //Get the current pixel
    @PIXEL
    D=M
    @SCREEN
    A=D+A
    //Change the pixel to black
    M=-1
    //Move to the next pixel
    @PIXEL
    M=M+1
    //Go to the Loop fot the next keyboard input
    @LOOP
    0;JMP
(END)
    @END
    0;JMP
