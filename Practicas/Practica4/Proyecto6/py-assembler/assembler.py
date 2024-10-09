#Implementacion del assembler
#Grupo ALU

import sys

dest = { 
    "null":"000", 
    "M":"001",
    "D":"010",
    "MD":"011", 
    "A":"100",
    "AM":"101",
    "AD":"110",
    "ADM":"111"
}

instructions = { 
    "0":"0101010", 
    "1":"0111111",
    "-1":"0111010",
    "D":"0001100", 
    "A":"0110000",
    "!D":"0001101",
    "!A":"0110001",
    "-D":"0001111",
    "-A":"0110011", 
    "D+1":"0011111",
    "A+1":"0110111",
    "D-1":"0001110",
    "A-1":"0110010",
    "D+A":"0000010", 
    "D-A":"0010011",
    "A-D":"0000111",
    "D&A":"0000000",
    "D|A":"0010101",

    "M":"1110000",
    "!M":"1110001",
    "-M":"1110011", 
    "M+1":"1110111",
    "M-1":"1110010",
    "D+M":"1000010",
    "D-M":"1010011",
    "M-D":"1000111",
    "D&M":"1000000",
    "D|M":"1010101",   
}

jump = { 
   "null":"000", 
    "JGT":"001",
    "JEQ":"010",
    "JGE":"011", 
    "JLT":"100",
    "JNE":"101",
    "JLE":"110",
    "JMP":"111"
}

symbols = {
    "R0":"0",
    "R1":"1",
    "R2":"2",
    "R3":"3",
    "R4":"4",
    "R5":"5",
    "R6":"6",
    "R7":"7",
    "R8":"8",
    "R9":"9",
    "R10":"10",
    "R11":"11",
    "R12":"12",
    "R13":"13",
    "R14":"14",
    "R15":"15",
    "SCREEN":"16384",
    "KBD":"24576",
    "SP":"0",
    "LCL": "1",
    "ARG":"2",
    "THIS":"3",
    "THAT":"4"
}

# Funcion para trabajar con instrucciones cortas (2 elementos, ej. 0; JMP) 
def short_command(tokenized): 
    loop = 2

    for value in range(2):
        tokenized[loop] = tokenized[loop-1]
        loop-=1
    
    tokenized[0] = None

# Funcion para rellenar un string con 000 para una longitud de 16 bits
def pad_string(value): 
    if (len(value) < 16): 
        pad = 16-len(value)
        return pad*"0" + value


# Funcion para convertir las instrucciones tokenizadas a binario teniendo en cuenta el tipo de instruccion (A o C)
def create_binary(tokenized, a_instruction): 

    destination = tokenized[0]
    comp = tokenized[1]
    jmp = tokenized[2] 
    a_inst = a_instruction
    address = "0"

    if (a_inst): 
        # Primero necesitamos revisar si hay simbolos para asignarles un valor
        if(check_symbol(jmp) is not None): 
            jmp = symbols.get(jmp)

        address = str(bin((int(jmp)))).replace("0b","")
        return pad_string(address)

    # Asume que la instruccion es de tipo C
    if destination is not None: 
        dest_binary = dest[destination]
    elif destination is None: 
        dest_binary = "000"
    if jmp is not None: 
        jmp_binary = jump[jmp]
    elif jmp is None: 
        jmp_binary="000"

    comp_binary = instructions[comp]

    return "111" + comp_binary + dest_binary + jmp_binary

# Funcion para revisar si un simbolo esta en la tabla de simbolos
def check_symbol(line):
    value_found = symbols.get(line)
    return value_found


if __name__ == "__main__": 

    import_file = sys.argv[1]

    print("Assembler running on file " + import_file)

    a_instruction = False

    # Crear la tabla inicial de simbolos

    f = open(import_file, "r")

    program_position = 0

    for line in f.readlines(): 

        line = line.strip() 

        if line == "": 
            continue
        if line[0] == "/":
            continue
        if line != "":
            if (line[0] == "("): 
                end = line.find(")")
                line = line.replace("(","")
                line = line.replace(")","")
                symbols[line[0:end-1]] = program_position
                continue
        program_position+=1

    f.close()

    # Con la tabla de simbolos ya creada pasar otra vez y reemplazarlos por sus direcciones de memoria
    
    f = open(import_file, "r")

    start_memory = 16

    for line in f.readlines(): 

        line = line.strip()
        line = line.replace(" ","")

        if line == "": 
            continue
        if line[0] == "/":
            continue

        if line != "":             
            if (line[0] == "@"):

                # Detectar conmentarion en linea (ej. codigo=1 //comentario)
                end = line.find("/")
                if (end==-1):
                    if (check_symbol(line[1:]) is None):
                        if not (line[1:].isdigit()):
                            symbols[line[1:]] = str(start_memory)
                            start_memory+=1
                elif (end>0): 
                     if (check_symbol(line[1:end]) is None):
                        if not (line[1:].isdigit()):
                            symbols[line[1:]] = str(start_memory)
                            start_memory+=1
    f.close()
       
    # Crear el archivo de output binario
    w = open("final.hack", "w")

    # Comenzar a procesar el archivo de input
    f = open(import_file, "r")
    for line in f.readlines(): 
        
        line = line.strip()   # Remover todo los whitespaces (espacios, tabs, lineas en blanco, etc)
        line = line.replace(" ","")
        
        character = ""
        process_line = True
        tokenized = [None] * 3
        token_point = 0
        next_token = False
        a_instruction = False
        assignment=False

        # Procesar y tokenizar cada linea
        # Tokenizar se refiere a dividir cada linea en sus elementos basicos dependiendo de si es una instruccion A o C

        if line == "": 
            process_line = False

        if (process_line):
            for x in line: 

                process_symbol = True

                if x == "/" and len(character)<1: 
                    process_line = False
                    break

                if x == "/" and len(character) >=1: 
                    break

                if x == "(": 
                    process_line = False
                    break
                    
                if x == "@": 
                    a_instruction = True;
                    tokenized[token_point] = "@"
                    token_point+=1
                    process_symbol = False
                    character = ""

                if x == "=": 
                    tokenized[token_point] = character
                    token_point +=1
                    process_symbol = False
                    character = ""
                    assignment = True


                if x == ";": 
                    tokenized[token_point] = character
                    token_point +=1
                    process_symbol = False
                    character = ""

                if x != " ":
                    if(process_symbol): 
                        character = character + x
        
        if(token_point < 3):
            tokenized[token_point] = character
            
        if(process_line):  # Ignorar comentarios

            # Llevar las instrucciones sin destinacion al lugar correcto
            
            if(token_point == 1 and not assignment): 
                short_command(tokenized)
            
            loops = 0
            # Comenzar la conversion a binario

            line_binary = create_binary(tokenized, a_instruction)


            # Escribir output al archivo .hack

            w.write(str(line_binary) + '\n')

    print("Assembler completado exitosamente: output es final.hack")

    f.close()
    w.close()



                




    
        

            




